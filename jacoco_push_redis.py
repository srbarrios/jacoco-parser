import xml.etree.ElementTree as ElementTree
import argparse
import redis

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test_name", help="Test Name", required=True)
parser.add_argument("-f", "--file_path", help="JaCoCo XML filepath", required=True)
parser.add_argument("-r", "--redis_host", help="Redis Host", required=True)
parser.add_argument("-p", "--redis_port", help="Redis Port", required=True)
parser.add_argument("-u", "--redis_username", help="Redis Username", required=True)
parser.add_argument("-w", "--redis_password", help="Redis Password", required=True)
args = parser.parse_args()

database = redis.Redis(
    host=args.redis_host,
    port=args.redis_port,
    username=args.redis_username,
    password=args.redis_password
)

tree = ElementTree.parse(args.file_path)
root = tree.getroot()
for package in root.findall('package'):
    package_name = package.get('name')
    for sourcefile in package.findall('sourcefile'):
        sourcefile_name = sourcefile.get('name')
        counter_class = sourcefile.find("./counter[@type='CLASS']")
        if counter_class is not None and int(counter_class.get('covered')) > 0:
            database.sadd(f'{package_name}/{sourcefile_name}', args.test_name)
