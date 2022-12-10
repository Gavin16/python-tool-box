
import redis

client = redis.StrictRedis(host="127.0.0.1")


if __name__ == '__main__':
    client.delete("codehole")
    for i in range(10000):
        client.execute_command("bf.add", "codehole", "user%d" % i)
        ret = client.execute_command("bf.exists", "codehole", "user%d" % i)
        if ret == 0:
            print(i)
            break
    print("结束执行！！！")
