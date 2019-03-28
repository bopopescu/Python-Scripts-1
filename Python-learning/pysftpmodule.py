import pysftp as sftp

def push_file_to_server():
    s = sftp.Connection(host="172.16.27.129", username = 'pnagwekar', password = 'ca$hc0w')

    local_path = "testme.txt"
    remote_path = "/home/pnagwekar/testme.txt"

    s.put(local_path, remote_path)
    s.close()

def pull_file_from_server():
    s = sftp.Connection(host="172.16.27.129", username='pnagwekar', password='ca$hc0w')

    local_path = "testme.txt"
    remote_path = "/home/pnagwekar/testme.txt"

    s.get(remote_path, local_path)
    s.close()

push_file_to_server()