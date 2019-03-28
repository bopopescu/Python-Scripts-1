import ssl
import requests
from pyvim.connect import SmartConnect, Disconnect
from cli_tools import *

def setup_args():
    parser = cli.build_arg_parser()
    parser.add_argument('-j', '--uuid', required=True,
                        help="UUID of the VirtualMachine you want to find."
                             " If -i is not used BIOS UUID assumed.")
    parser.add_argument('-i', '--instance', required=False,
                        action='store_true',
                        help="Flag to indicate the UUID is an instance UUID")
    parser.add_argument('-d', '--description', required=False,
                        help="Description for the snapshot")
    parser.add_argument('-n', '--name', required=True,
                        help="Name for the Snapshot")
    my_args = parser.parse_args()
    return cli_tools.prompt_for_password(my_args)

def main():
    sslContext = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    sslContext.verify_mode = ssl.CERT_NONE
    requests.packages.urllib3.disable_warnings()

    args = setup_args()
    h="w2-vcopsqe-001.eng.vmware.com"
    si= SmartConnect(host=h,port=443,user='root',pwd='ca$hc0w',sslContext=sslContext)

# start this thing
if __name__ == "__main__":
    main()
