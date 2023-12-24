/* 

Fabio Akita: https://youtu.be/-yGHG3pnHLg?si=PEkmQpwxUCgCSgr8
Quem nunca sentiu dor, nunca aprendeu nada. E nesta rinha, a versão disso é essa limitação de recursos, 
senão, claro, o participante com uma máquina como a minha, 
com 64 giga de RAM, Ryzen 9 de 32 threads, 
facilmente conseguiria gerar resultados com números muito melhores que todo mundo. 
Mas com esse limite, o participante com um quad core de 4 giga de RAM poderia ultrapassar
minha máquina, se soubesse administrar melhor os recursos limitados. E isso de limitar recursos no Docker, 
não foi feito pra concursos.

*/

//meta 1) rodar primo mais rapido que primo compilado em tempo real


//meta 2) rodar crud mais rapido que o pai do LMAX
//meta 3) rodar crud com prevayler mais rapido que LMAX
//meta 4) bater rinha de back end com poco f1 mais experto que o 


// Callback handler which can be implemented by consumers
final BatchHandler<ValueEntry> batchHandler = new BatchHandler<ValueEntry>()
{
public void onAvailable(final ValueEntry entry) throws Exception
{
// process a new entry as it becomes available.
}

    public void onEndOfBatch() throws Exception
    {
        // useful for flushing results to an IO device if necessary.
    }

    public void onCompletion()
    {
        // do any necessary clean up before shutdown
    }
};

RingBuffer<ValueEntry> ringBuffer =
    new RingBuffer<ValueEntry>(ValueEntry.ENTRY_FACTORY, SIZE,
                               ClaimStrategy.Option.SINGLE_THREADED,
                               WaitStrategy.Option.YIELDING);
ConsumerBarrier<ValueEntry> consumerBarrier = ringBuffer.createConsumerBarrier();
BatchConsumer<ValueEntry> batchConsumer =
    new BatchConsumer<ValueEntry>(consumerBarrier, batchHandler);
ProducerBarrier<ValueEntry> producerBarrier = ringBuffer.createProducerBarrier(batchConsumer);

// Each consumer can run on a separate thread
EXECUTOR.submit(batchConsumer);

// Producers claim entries in sequence
ValueEntry entry = producerBarrier.nextEntry();

// copy data into the entry container

// make the entry available to consumers
producerBarrier.commit(entry);