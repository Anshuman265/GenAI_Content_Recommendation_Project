
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class UserActivityProducer {

    private KafkaProducer<String, String> producer;
    
    public UserActivityProducer() {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        this.producer = new KafkaProducer<>(props);
    }

    public void sendUserActivity(String userId, String activity) {
        ProducerRecord<String, String> record = new ProducerRecord<>("user-activities", userId, activity);
        producer.send(record);
    }
    
    public void close() {
        producer.close();
    }
}
