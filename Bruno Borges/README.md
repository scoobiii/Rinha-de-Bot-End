//-------- PessoaResource.java


package org.acme;

import static java.util.Collections.emptyList;

import java.util.Arrays;
import java.util.List;
import java.util.UUID;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


import io.quarkus.hibernate.reactive.panache.Panache;
import io.quarkus.hibernate.reactive.panache.common.WithSession;
import io.smallrye.mutiny.Uni;
import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.QueryParam;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.Response.Status;


@Path("/")
public class PessoaResource {

    private static final Logger logger = LoggerFactory.getLogger(PessoaResource.class);


    @Inject
    CacheService cache;


    @GET
    @Path("/pessoas")
    @Produces(MediaType.APPLICATION_JSON)
    @WithSession
    public Uni<Response> findTop50(@QueryParam("t") String termo) {
        //logger.info("### Buscando pessoa: {} ", termo);

        if (termo == null || termo.isBlank()) {
            return Uni.createFrom().item(Response.status(Status.BAD_REQUEST).build());
        }

        List<Pessoas> foundInCache = cache.search(termo);
        
        if (foundInCache != null){
            //logger.info("### Buscando no CACHE: {} ", termo);
            return Uni.createFrom().item(Response.ok(foundInCache).build());
        } else{
            logger.info("### Buscando no banco de dados: {} ", termo);
             return Pessoas.<Pessoas>find("busca like '%' || ?1 || '%'", termo).page(0, 50).list()
                    .onItem().ifNotNull().transform(entity -> Response.ok(entity).build())
                    .onItem().ifNull().continueWith(Response.status(Status.NOT_FOUND)::build);
        }
       
    }

    @POST
    @Path("/pessoas")
    @Produces(MediaType.APPLICATION_JSON)
    public Uni<Response> create(Pessoas pessoa) {

        try {

            String apelido = pessoa.getApelido();
            String nome = pessoa.getNome();

            if (apelido == null || apelido.isBlank() || apelido.length() > 32
                    || nome == null || nome.isBlank() || nome.length() > 100 
                    || invalidStack(pessoa.getStack())
                    ) {
                //logger.info("### Apelido fora do padrao permitido");
                return Uni.createFrom().item(Response.status(Status.BAD_REQUEST).build());
            }

            if (pessoaByApelidoExists(pessoa.getApelido())) {
                return Uni.createFrom().item(Response.status(422).build());
            }

            var uuid = UUID.randomUUID();
            //logger.info("Gerando UUID: {}", uuid);

            pessoa.setId(uuid);
            cache.insertPessoa(pessoa);

            return Panache
                    .withTransaction(pessoa::persist)
                    .replaceWith(Response.status(Status.CREATED).entity(pessoa)
                    .header("Location", "/pessoas/" + uuid.toString())
                    .build());
                    
        } catch (Exception e) {
            logger.error("### ERRO: {}", e.getMessage());
            return Uni.createFrom().item(Response.status(Status.INTERNAL_SERVER_ERROR).build());
        }                    
    }

    
    @GET
    @Path("/pessoas/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    @WithSession
    public Uni<Response> get(@PathParam("id") String id) {

        try {
        
            var foundInCache = cache.getPessoa(id);
            //logger.info("Buscando ID {}", id);

            if (foundInCache != null) {
                //logger.info("Registro encontrado em Cache: " + id);
                return Uni.createFrom().item(Response.ok(foundInCache).build());
            } else {
                //logger.info("Buscando registro do banco de dados: " + id);
                return Pessoas.<Pessoas>findById(UUID.fromString(id))
                        .onItem().ifNotNull().transform(entity -> Response.ok(entity).build())
                        .onItem().ifNull().continueWith(Response.status(Status.NOT_FOUND)::build);
                
            }

        } catch (Exception e) {
            logger.error("### ERRO: {}", e.getMessage());
            return Uni.createFrom().item(Response.status(Status.INTERNAL_SERVER_ERROR).build());
        }
        
    }

   
    @GET
    @Path("/contagem-pessoas")
    @WithSession
    public Uni<Long> count() {
        return Pessoas.count();
    }

    private boolean pessoaByApelidoExists(String apelido) {
        return (cache.apelidoExists(apelido)) ;
    }

    public List<String> convertToEntityAttribute(String string) {
        return string != null ? Arrays.asList(string.split(";")) : emptyList();
    }


    private boolean invalidStack(List<String> stack) {
        if (stack == null) {
            return false;
        }

        for (String s : stack) {
            if (s.length() > 32) {
                return true;
            }
        }

        return false;
    }

}


//""" ---------StringListConverter.java


package org.acme;

import jakarta.persistence.AttributeConverter;
import jakarta.persistence.Converter;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

@Converter
public class StringListConverter implements AttributeConverter<List<String>, String> {

    private static final String DELIMITER = ",";

    @Override
    public String convertToDatabaseColumn(List<String> attribute) {
        if (attribute == null || attribute.isEmpty()) {
            return null;
        }
        return String.join(DELIMITER, attribute);
    }

    @Override
    public List<String> convertToEntityAttribute(String dbData) {
        if (dbData == null || dbData.isEmpty()) {
            return Collections.emptyList();
        }
        return Arrays.asList(dbData.split(DELIMITER));
    }
}



//---------Pessoas.java


package org.acme;

import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.UUID;

import org.hibernate.annotations.Generated;

import com.fasterxml.jackson.annotation.JsonIgnore;

import io.quarkus.hibernate.reactive.panache.PanacheEntity;
import io.quarkus.hibernate.reactive.panache.PanacheEntityBase;
import jakarta.persistence.Cacheable;
import jakarta.persistence.Column;
import jakarta.persistence.Convert;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "PESSOAS")
@Cacheable
public class Pessoas extends PanacheEntityBase {
    
    @Id
    @Column(name = "ID")
    //@GeneratedValue
    private UUID id;

    @Column(name = "APELIDO")
    private String apelido;

    @Column(name = "NOME")
    private String nome;

    @Column(name = "NASCIMENTO")
    private String nascimento;

    @Column(name = "STACK" )
    @Convert(converter = StringListConverter.class)
    private List<String> stack = Collections.emptyList();

    @Column(name = "BUSCA_TRGM")
    @Generated
    @JsonIgnore
    public String busca;

    public UUID getId() {
        return id;
    }

    public void setId(UUID idUUID) {
        this.id = idUUID;
    }

    public String getApelido() {
        return apelido;
    }

    public void setApelido(String apelido) {
        this.apelido = apelido;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNascimento() {
        return nascimento;
    }

    public void setNascimento(String nascimento) {
        this.nascimento = nascimento;
    }

    public List<String> getStack() {
        return stack;
    }

    public void setStack(List<String> stack) {
        if (stack == null) {
            stack = Collections.emptyList();
        }
        this.stack = stack;
    }

 }

 //-------------------------TestJson

 package org.acme;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.UUID;

import org.junit.jupiter.api.Test;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import io.quarkus.test.junit.QuarkusTest;

@QuarkusTest
public class TestJson {
    
    @Test
    public void testPessoaToJson() throws JsonProcessingException {
        Pessoas pessoa = new Pessoas();
        //pessoa.setId(UUID.randomUUID());
        pessoa.setApelido("apelido");
        pessoa.setNome("nome");
        pessoa.setNascimento("nascimento");
        pessoa.setStack(Arrays.asList("Java", "Python"));

        // using jackson objectmapper, convert pessoa to json string
        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(pessoa);
        
        // using jackson objectmapper, convert json string to pessoa
        Pessoas pessoa2 = mapper.readValue(json, Pessoas.class);

        //assertEquals(pessoa, pessoa2);
    }

}



  //-------------------------------docker-composer

  version: '3.9'
#name: 'rinha-brunoborges'

services:
  api1:
    build:
      context: .
      dockerfile: src/main/docker/Dockerfile.jvm
    hostname: api1
    environment:
      - SERVER_PORT=8080
      - DATABASE_URL=vertx-reactive:postgresql://localhost:5432/rinhadb
      - DATABASE_USERNAME=rinha
      - DATABASE_PASSWORD=rinha123
    depends_on:
      db-postgresql:
        condition: service_healthy
    ulimits:
      nofile:
        soft: 1000000
        hard: 1000000
    deploy:
      resources:
        limits:
          cpus: '0.35'
          memory: '512MB'
    healthcheck:
      test: curl -o /dev/null -s --retry 0 --head http://localhost:8080/ || exit 1
      interval: 10s
      retries: 60
      start_period: 20s
      timeout: 5s
    network_mode: "host"  
    # networks:
    #   - "app-network"

  api2:
    build:
      context: .
      dockerfile: src/main/docker/Dockerfile.jvm
    hostname: api2
    environment:
      - SERVER_PORT=8090
      - DATABASE_URL=vertx-reactive:postgresql://localhost:5432/rinhadb
      - DATABASE_USERNAME=rinha
      - DATABASE_PASSWORD=rinha123
    # ports:
    #   - "8090:8080"  
    depends_on:
      db-postgresql:
        condition: service_healthy
    ulimits:
      nofile:
        soft: 1000000
        hard: 1000000
    deploy:
      resources:
        limits:
          cpus: '0.35'
          memory: '512MB'
    healthcheck:
      test: curl -o /dev/null -s --retry 0 --head http://localhost:8090/ || exit 1
      interval: 10s
      retries: 60
      start_period: 20s
      timeout: 5s
    network_mode: "host"    
    # networks:
    #   - "app-network"

  nginx:
    image: nginx:latest
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      api1:
        condition: service_healthy
      api2:
        condition: service_healthy
    ports:
      - "9999:9999"
    ulimits:
          nofile:
            soft: 1000000
            hard: 1000000
    deploy:
      resources:
        limits:
          cpus: '0.9'
          memory: '0.5GB'
    logging:
      driver: "json-file"
      options:
        max-size: "10m"  # Tamanho máximo do arquivo de log
        max-file: "10"     # Número máximo de arquivos de log
    network_mode: "host"
    # networks:
    #   - "app-network"

  db-postgresql:
    image: postgres:latest
    hostname: db-postgresql
    environment:
      - POSTGRES_PASSWORD=rinha123
      - POSTGRES_USER=rinha
      - POSTGRES_DB=rinhadb
     # - POSTGRES_INITDB_ARGS=--data-checksums=off  # Desligar data checksums para melhorar a inserção de dados
    ports:
      - "5432:5432"
    volumes:
      - ./ddl.sql:/docker-entrypoint-initdb.d/ddl.sql
      - ./postgresql.conf:/etc/postgresql/postgresql.conf # Mapeie o arquivo de configuração
    command: postgres -c config_file=/etc/postgresql/postgresql.conf # Use o caminho correto no comando
    deploy:
      resources:
        limits:
          cpus: '0.9'
          memory: '1.5GB'
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 5s
      timeout: 5s
      retries: 20
      start_period: 10s
    network_mode: "host"
    # networks:
    #   - "app-network"
    

  # pgadmin:
  #   container_name: pgadmin
  #   hostname: pgadmin
  #   image: dpage/pgadmin4
  #   restart: unless-stopped
  #   environment:
  #     - PGADMIN_DEFAULT_EMAIL=admin@admin.com
  #     - PGADMIN_DEFAULT_PASSWORD=admin
  #   ports:
  #     - "5050:80"
  #   depends_on:
  #     - db-postgresql
  #   # network_mode: "bridge"  
  #   networks:
  #     - app-network  

# networks:
#   app-network:

# networks:
#   app-network:
    # driver: host
    # external: true

   //--------------------------

   worker_processes auto;
# worker_rlimit_nofile 500000;

events {
    use epoll;
    worker_connections 50000;
}


http {
    access_log off;
    # error_log on;
    gzip off;

    upstream api {
        keepalive 250;
        server localhost:8080;
        server localhost:8090;
    }

    server {
        listen 9999;

        location / {
            proxy_read_timeout 300s;   # Aumente conforme necessário
            proxy_send_timeout 300s;   # Aumente conforme necessário
            proxy_buffering off;
            proxy_set_header Connection "";
            proxy_http_version 1.1;
            proxy_set_header Keep-Alive "";
            proxy_set_header Proxy-Connection "keep-alive";
            proxy_pass http://api;
        }
    }
}




    //----------------------------maven




#!/bin/sh
# ----------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Maven Start Up Batch script
#
# Required ENV vars:
# ------------------
#   JAVA_HOME - location of a JDK home dir
#
# Optional ENV vars
# -----------------
#   M2_HOME - location of maven2's installed home dir
#   MAVEN_OPTS - parameters passed to the Java VM when running Maven
#     e.g. to debug Maven itself, use
#       set MAVEN_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000
#   MAVEN_SKIP_RC - flag to disable loading of mavenrc files
# ----------------------------------------------------------------------------

if [ -z "$MAVEN_SKIP_RC" ] ; then

  if [ -f /usr/local/etc/mavenrc ] ; then
    . /usr/local/etc/mavenrc
  fi

  if [ -f /etc/mavenrc ] ; then
    . /etc/mavenrc
  fi

  if [ -f "$HOME/.mavenrc" ] ; then
    . "$HOME/.mavenrc"
  fi

fi

# OS specific support.  $var _must_ be set to either true or false.
cygwin=false;
darwin=false;
mingw=false
case "`uname`" in
  CYGWIN*) cygwin=true ;;
  MINGW*) mingw=true;;
  Darwin*) darwin=true
    # Use /usr/libexec/java_home if available, otherwise fall back to /Library/Java/Home
    # See https://developer.apple.com/library/mac/qa/qa1170/_index.html
    if [ -z "$JAVA_HOME" ]; then
      if [ -x "/usr/libexec/java_home" ]; then
        export JAVA_HOME="`/usr/libexec/java_home`"
      else
        export JAVA_HOME="/Library/Java/Home"
      fi
    fi
    ;;
esac

if [ -z "$JAVA_HOME" ] ; then
  if [ -r /etc/gentoo-release ] ; then
    JAVA_HOME=`java-config --jre-home`
  fi
fi

if [ -z "$M2_HOME" ] ; then
  ## resolve links - $0 may be a link to maven's home
  PRG="$0"

  # need this for relative symlinks
  while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
      PRG="$link"
    else
      PRG="`dirname "$PRG"`/$link"
    fi
  done

  saveddir=`pwd`

  M2_HOME=`dirname "$PRG"`/..

  # make it fully qualified
  M2_HOME=`cd "$M2_HOME" && pwd`

  cd "$saveddir"
  # echo Using m2 at $M2_HOME
fi

# For Cygwin, ensure paths are in UNIX format before anything is touched
if $cygwin ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --unix "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --unix "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# For Mingw, ensure paths are in UNIX format before anything is touched
if $mingw ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME="`(cd "$M2_HOME"; pwd)`"
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME="`(cd "$JAVA_HOME"; pwd)`"
fi

if [ -z "$JAVA_HOME" ]; then
  javaExecutable="`which javac`"
  if [ -n "$javaExecutable" ] && ! [ "`expr \"$javaExecutable\" : '\([^ ]*\)'`" = "no" ]; then
    # readlink(1) is not available as standard on Solaris 10.
    readLink=`which readlink`
    if [ ! `expr "$readLink" : '\([^ ]*\)'` = "no" ]; then
      if $darwin ; then
        javaHome="`dirname \"$javaExecutable\"`"
        javaExecutable="`cd \"$javaHome\" && pwd -P`/javac"
      else
        javaExecutable="`readlink -f \"$javaExecutable\"`"
      fi
      javaHome="`dirname \"$javaExecutable\"`"
      javaHome=`expr "$javaHome" : '\(.*\)/bin'`
      JAVA_HOME="$javaHome"
      export JAVA_HOME
    fi
  fi
fi

if [ -z "$JAVACMD" ] ; then
  if [ -n "$JAVA_HOME"  ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
      # IBM's JDK on AIX uses strange locations for the executables
      JAVACMD="$JAVA_HOME/jre/sh/java"
    else
      JAVACMD="$JAVA_HOME/bin/java"
    fi
  else
    JAVACMD="`\\unset -f command; \\command -v java`"
  fi
fi

if [ ! -x "$JAVACMD" ] ; then
  echo "Error: JAVA_HOME is not defined correctly." >&2
  echo "  We cannot execute $JAVACMD" >&2
  exit 1
fi

if [ -z "$JAVA_HOME" ] ; then
  echo "Warning: JAVA_HOME environment variable is not set."
fi

CLASSWORLDS_LAUNCHER=org.codehaus.plexus.classworlds.launcher.Launcher

# traverses directory structure from process work directory to filesystem root
# first directory with .mvn subdirectory is considered project base directory
find_maven_basedir() {

  if [ -z "$1" ]
  then
    echo "Path not specified to find_maven_basedir"
    return 1
  fi

  basedir="$1"
  wdir="$1"
  while [ "$wdir" != '/' ] ; do
    if [ -d "$wdir"/.mvn ] ; then
      basedir=$wdir
      break
    fi
    # workaround for JBEAP-8937 (on Solaris 10/Sparc)
    if [ -d "${wdir}" ]; then
      wdir=`cd "$wdir/.."; pwd`
    fi
    # end of workaround
  done
  echo "${basedir}"
}

# concatenates all lines of a file
concat_lines() {
  if [ -f "$1" ]; then
    echo "$(tr -s '\n' ' ' < "$1")"
  fi
}

BASE_DIR=`find_maven_basedir "$(pwd)"`
if [ -z "$BASE_DIR" ]; then
  exit 1;
fi

##########################################################################################
# Extension to allow automatically downloading the maven-wrapper.jar from Maven-central
# This allows using the maven wrapper in projects that prohibit checking in binary data.
##########################################################################################
if [ -r "$BASE_DIR/.mvn/wrapper/maven-wrapper.jar" ]; then
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Found .mvn/wrapper/maven-wrapper.jar"
    fi
else
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Couldn't find .mvn/wrapper/maven-wrapper.jar, downloading it ..."
    fi
    if [ -n "$MVNW_REPOURL" ]; then
      jarUrl="$MVNW_REPOURL/org/apache/maven/wrapper/maven-wrapper/3.1.1/maven-wrapper-3.1.1.jar"
    else
      jarUrl="https://repo.maven.apache.org/maven2/org/apache/maven/wrapper/maven-wrapper/3.1.1/maven-wrapper-3.1.1.jar"
    fi
    while IFS="=" read key value; do
      case "$key" in (wrapperUrl) jarUrl="$value"; break ;;
      esac
    done < "$BASE_DIR/.mvn/wrapper/maven-wrapper.properties"
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Downloading from: $jarUrl"
    fi
    wrapperJarPath="$BASE_DIR/.mvn/wrapper/maven-wrapper.jar"
    if $cygwin; then
      wrapperJarPath=`cygpath --path --windows "$wrapperJarPath"`
    fi

    if command -v wget > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found wget ... using wget"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            wget "$jarUrl" -O "$wrapperJarPath" || rm -f "$wrapperJarPath"
        else
            wget --http-user=$MVNW_USERNAME --http-password=$MVNW_PASSWORD "$jarUrl" -O "$wrapperJarPath" || rm -f "$wrapperJarPath"
        fi
    elif command -v curl > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found curl ... using curl"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            curl -o "$wrapperJarPath" "$jarUrl" -f
        else
            curl --user $MVNW_USERNAME:$MVNW_PASSWORD -o "$wrapperJarPath" "$jarUrl" -f
        fi

    else
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Falling back to using Java to download"
        fi
        javaClass="$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.java"
        # For Cygwin, switch paths to Windows format before running javac
        if $cygwin; then
          javaClass=`cygpath --path --windows "$javaClass"`
        fi
        if [ -e "$javaClass" ]; then
            if [ ! -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Compiling MavenWrapperDownloader.java ..."
                fi
                # Compiling the Java class
                ("$JAVA_HOME/bin/javac" "$javaClass")
            fi
            if [ -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                # Running the downloader
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Running MavenWrapperDownloader.java ..."
                fi
                ("$JAVA_HOME/bin/java" -cp .mvn/wrapper MavenWrapperDownloader "$MAVEN_PROJECTBASEDIR")
            fi
        fi
    fi
fi
##########################################################################################
# End of extension
##########################################################################################

export MAVEN_PROJECTBASEDIR=${MAVEN_BASEDIR:-"$BASE_DIR"}
if [ "$MVNW_VERBOSE" = true ]; then
  echo $MAVEN_PROJECTBASEDIR
fi
MAVEN_OPTS="$(concat_lines "$MAVEN_PROJECTBASEDIR/.mvn/jvm.config") $MAVEN_OPTS"

# For Cygwin, switch paths to Windows format before running java
if $cygwin; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --path --windows "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --path --windows "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
  [ -n "$MAVEN_PROJECTBASEDIR" ] &&
    MAVEN_PROJECTBASEDIR=`cygpath --path --windows "$MAVEN_PROJECTBASEDIR"`
fi

# Provide a "standardized" way to retrieve the CLI args that will
# work with both Windows and non-Windows executions.
MAVEN_CMD_LINE_ARGS="$MAVEN_CONFIG $@"
export MAVEN_CMD_LINE_ARGS

WRAPPER_LAUNCHER=org.apache.maven.wrapper.MavenWrapperMain

exec "$JAVACMD" \
  $MAVEN_OPTS \
  $MAVEN_DEBUG_OPTS \
  -classpath "$MAVEN_PROJECTBASEDIR/.mvn/wrapper/maven-wrapper.jar" \
  "-Dmaven.home=${M2_HOME}" \
  "-Dmaven.multiModuleProjectDirectory=${MAVEN_PROJECTBASEDIR}" \
  ${WRAPPER_LAUNCHER} $MAVEN_CONFIG "$@"


     //-----------------------pom


     <?xml version="1.0"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.acme</groupId>
  <artifactId>code-with-quarkus</artifactId>
  <version>1.0.0-SNAPSHOT</version>
  <properties>
    <compiler-plugin.version>3.11.0</compiler-plugin.version>
    <maven.compiler.release>17</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
    <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>
    <quarkus.platform.version>3.3.2</quarkus.platform.version>
    <skipITs>true</skipITs>
    <surefire-plugin.version>3.0.0</surefire-plugin.version>
  </properties>
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>${quarkus.platform.group-id}</groupId>
        <artifactId>${quarkus.platform.artifact-id}</artifactId>
        <version>${quarkus.platform.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>
  <dependencies>
    
    <!-- <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-arc</artifactId>
    </dependency> -->

      <!-- REACTIVE ==================================================== -->
      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-hibernate-reactive-panache</artifactId>
      </dependency>

      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-reactive-pg-client</artifactId>
      </dependency>

      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-resteasy-reactive-jackson</artifactId>
      </dependency>
      <!-- REACTIVE ==================================================== -->
      
      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-smallrye-health</artifactId>
      </dependency>

      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-smallrye-metrics</artifactId>
      </dependency>

      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-smallrye-fault-tolerance</artifactId>
      </dependency>

      <dependency>
          <groupId>io.quarkus</groupId>
          <artifactId>quarkus-smallrye-openapi</artifactId>
      </dependency>

    <!-- <dependency>
      <groupId>io.quarkiverse.jooq</groupId>
      <artifactId>quarkus-jooq</artifactId>
      <version>2.0.0</version>
    </dependency> -->
    
    <!-- <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-scheduler</artifactId>
    </dependency>
     -->
    <dependency>
      <groupId>io.quarkus</groupId>
      <artifactId>quarkus-junit5</artifactId>
      <scope>test</scope>
    </dependency>
    
    <dependency>
      <groupId>io.rest-assured</groupId>
      <artifactId>rest-assured</artifactId>
      <scope>test</scope>
    </dependency>
    
    <!-- <dependency>
      <groupId>org.jooq</groupId>
      <artifactId>jooq</artifactId>
      <version>3.18.6</version>
    </dependency> -->

    <!-- <dependency>
      <groupId>org.postgresql</groupId>
      <artifactId>postgresql</artifactId>
      <version>42.6.0</version>
    </dependency> -->

  </dependencies>
  <build>
    <plugins>
        <plugin>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>${compiler-plugin.version}</version>
        </plugin>
        <plugin>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>${surefire-plugin.version}</version>
                
            <configuration>
                
                <skipTests>${skipTests}</skipTests>

                <systemPropertyVariables>
                    <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
                    <maven.home>${maven.home}</maven.home>
                </systemPropertyVariables>
            </configuration>
        </plugin>
        <plugin>
            <groupId>${quarkus.platform.group-id}</groupId>
            <artifactId>quarkus-maven-plugin</artifactId>
            <version>${quarkus.platform.version}</version>
            <executions>
                <execution>
                    <goals>
                        <goal>build</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
<profiles>
    <profile>
        <id>native</id>
        <activation>
            <property>
                <name>native</name>
            </property>
        </activation>
        <properties>
            <quarkus.package.type>native</quarkus.package.type>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-failsafe-plugin</artifactId>
                    <version>${surefire-plugin.version}</version>
                    <executions>
                        <execution>
                            <goals>
                                <goal>integration-test</goal>
                                <goal>verify</goal>
                            </goals>
                            <configuration>
                                <systemPropertyVariables>
                                    <native.image.path>${project.build.directory}/${project.build.finalName}-runner</native.image.path>
                                    <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
                                    <maven.home>${maven.home}</maven.home>
                                </systemPropertyVariables>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
</project>







      //-----------------------------README


      # Rinha de Backend

Desafio original:
https://github.com/zanfranceschi/rinha-de-backend-2023-q3?s=08


# By Bruno Borges e Vinícius Ferraz
Melhoria no código do projeto rinha-de-backend originário do repositório:

* Git do Bruno
https://github.com/brunoborges/rinha-app

* Git do Vinícuus
https://github.com/viniciusfcf/rinha-de-backend-2023-q3/tree/main/quarkus-app-revanche


## Atenção!!!
Antes do build criar arquivo .env com as variáveis:
DATABASE_USERNAME=
DATABASE_PASSWORD=
DATABASE_URL=
SERVER_PORT=

## ✔️ Required
* Maven: 3.8.4
* Java version: 17
* Docker version: 20.10.17
* Docker-compose version: v2.2.2

# Sobre:
Projeto backend feito em Quarkus 3.3.1 seguindo as regras:
https://github.com/zanfranceschi/rinha-de-backend-2023-q3/blob/main/INSTRUCOES.md


## 💻 Getting started

```bash
# Build 
$ mvn clean package

# Local execution
$ mvn quarkus:dev -Ddebug=false
```


## Getting started Docker
```bash

# Started and attaches to containers for a service
$ docker-compose up --build
```


## Getting started Docker (Native Image)
```bash
# Install image from file build_docker_push.sh 
$ ./build_docker_native.sh 

# Started and attaches to containers for a service
$ docker-compose -f docker-compose-native.yml --env-file ./.env up
```






## Ajustes realizados:

* Ajuste no Script DDL com obrigatoriedade somente no campo apelido
* Ajuste no cache local para 100k (Total de registros do teste de stress)
* Busca de dados no cache, caso contrário, faz busca no bando de dados
* Aumento de sessões do Postgres para 400 e cada POD com 150 sessões simultâneas



## Resultado obtidos

* Docker stats:

![image](https://github.com/zsantana/rinha-backend-by-bruno-borges/assets/17239827/b494d062-c8ad-4299-93cf-c264e68910ee)


* Resultado e performance:

![image](https://github.com/zsantana/rinha-backend-by-bruno-borges/assets/17239827/3675a4b7-6f06-4b55-b09d-64074562aa99)



* Requisições por segundos:
![image](https://github.com/zsantana/rinha-backend-by-bruno-borges/assets/17239827/c4339b73-778c-4cfb-9031-6a49d8b97e15)



       //-----------------------------------run-gatlin.sh


       #!/bin/sh
WORKSPACE=$(pwd)/rinha-de-backend-2023-q3/stress-test/user-files

if [ ! -d "rinha-de-backend-2023-q3" ]; then
    echo "rinha-de-backend-2023-q3 not found. Downloading..."
    git clone --depth=1 --branch=main --quiet https://github.com/zanfranceschi/rinha-de-backend-2023-q3
else
    echo "rinha-de-backend-2023-q3 found. Updating..."
    cd rinha-de-backend-2023-q3
    git pull --quiet
    cd ..
fi

cd rinha-de-backend-2023-q3

# check if directory gatling-charts-highcharts-bundle exists. if it doesnt, then download and unzip
if [ ! -d "gatling-charts-highcharts-bundle-3.9.5" ]; then
    echo "gatling-charts-highcharts-bundle-3.9.5 not found. Downloading..."
    wget --no-verbose https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/3.9.5/gatling-charts-highcharts-bundle-3.9.5-bundle.zip
    unzip gatling-charts-highcharts-bundle-3.9.5-bundle.zip
fi

cd gatling-charts-highcharts-bundle-3.9.5
./bin/gatling.sh -rm local -s RinhaBackendSimulation -rd "DESCRICAO" -rf $WORKSPACE/results -sf $WORKSPACE/simulations -rsf $WORKSPACE/resources
echo GATLING_OUTPUT_FOLDER=$(ls $WORKSPACE/results | sort | head -n 1)

cd ..

curl -i http://localhost:9999/contagem-pessoas

echo "\nEOF"



        //----------------------------ddl.sql

         SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', 'public', false); -- Defina o esquema como 'public' aqui
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER SCHEMA PUBLIC OWNER TO rinha;

SET default_tablespace = '';

SET default_table_access_method = heap;

DROP TABLE IF EXISTS public.PESSOAS;

CREATE TABLE public.PESSOAS (
    ID uuid NOT NULL,
    APELIDO VARCHAR(32) UNIQUE NOT NULL,
    NASCIMENTO VARCHAR(12) NOT NULL,
    NOME VARCHAR(100) NOT NULL,
    STACK VARCHAR(255),
    PRIMARY KEY (ID),
    BUSCA_TRGM TEXT GENERATED ALWAYS AS (
        NOME || ' ' || APELIDO || ' ' || COALESCE(STACK, '')
    ) STORED NOT NULL
);

CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Defina o esquema 'public' novamente antes de criar o índice
SELECT pg_catalog.set_config('search_path', 'public', false);

CREATE INDEX CONCURRENTLY IF NOT EXISTS IDX_PESSOAS_BUSCA_TGRM ON public.PESSOAS USING GIST (BUSCA_TRGM GIST_TRGM_OPS(siglen=256)) 
INCLUDE(apelido, nascimento, nome, ID, stack);

ALTER TABLE public.PESSOAS OWNER TO rinha;



//----------------------------------postgresql.conf

listen_addresses='*'
max_connections=350
superuser_reserved_connections=3
unix_socket_directories='/var/run/postgresql'
shared_buffers=512MB
work_mem=4MB
maintenance_work_mem=256MB
effective_cache_size=1GB
wal_buffers=64MB
checkpoint_timeout=10min
checkpoint_completion_target=0.9
random_page_cost=4.0
effective_io_concurrency=10
autovacuum=on
log_statement='none'
log_duration=off
log_lock_waits=on
log_error_verbosity=terse
log_min_messages=panic
log_min_error_statement=panic
