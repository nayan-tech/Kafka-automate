from kafka import KafkaProducer
import argparse

producer = KafkaProducer(bootstrap_servers='localhost:9092')

parser= argparse.ArgumentParser()

parser.add_argument('--video_id', action= 'store', type= str, default= 'Test')
parser.add_argument('--user_id', action= 'store', type= str, default= 'Test')

args, unknown = parser.parse_known_args()

video_id = args.video_id
user_id = args.user_id

kafka_message = '{"violationId":"' + video_id + '", "video_path": "/var/shared_data/videos/' + video_id + '.mp4", "det_path": "/var/shared_data/dets/initial/' + video_id \
    + '_veh.txt", "postedBy": "' + user_id + '", "videoId": "' + video_id + '", "modelVersion": "vd_1.0.0.0:"}'

print("message: ", kafka_message)

producer.send('videos_dev', kafka_message.encode('utf-8'))
producer.flush()
