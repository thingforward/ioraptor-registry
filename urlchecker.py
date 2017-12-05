import requests
import json
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
        for filename in os.listdir("./packages"):
                if filename.endswith(".json"):
                        checkUrls(filename)
                        continue
                else:
                        continue

def checkUrls(file):
        json_data=open("./packages/"+file).read()
        data = json.loads(json_data)
        platformFail = False

        print(bcolors.HEADER+"Testing file: "+file+bcolors.ENDC)

        #lnx_i386
        try:
                platform = "lnx_i386"
                lnx_i386_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(lnx_i386_url)
                s = platform+" : "+lnx_i386_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        #lnx_x86_64
        try:
                platform = "lnx_x86_64"
                lnx_x86_64_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(lnx_x86_64_url)
                s = platform+" : "+lnx_x86_64_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                       else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)
        
        #lnx_i386
        try:
                platform = "lnx_i386"
                lnx_i386_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(lnx_i386_url)
                s = platform+" : "+lnx_i386_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        #lnx_x86_64
        try:
                platform = "lnx_x86_64"
                lnx_x86_64_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(lnx_x86_64_url)
                s = platform+" : "+lnx_x86_64_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        #osx_x86_64
        try:
                platform = "osx_x86_64"
                osx_x86_64_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(osx_x86_64_url)
                s = platform+" : "+osx_x86_64_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        #win_i386
        try:
                platform = "win_i386"
                win_i386_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(win_i386_url)
                s = platform+" : "+win_i386_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        #win_x86_64
        try:
                platform = "win_x86_64"
                win_x86_64_url = data.get(platform).get('urls').get('executable')
                resp = requests.head(win_x86_64_url)
                s = platform+" : "+win_x86_64_url+" : "
                if(resp.status_code != 200):
                        s += bcolors.FAIL
                        platformFail = True
                else:
                        s += bcolors.OKGREEN

                s += str(resp.status_code)+bcolors.ENDC
                print(s)
        except Exception as e:
                platformFail = True
                print(e)

        if(platformFail):
                print(bcolors.FAIL+"This file had a faulty URL!"+bcolors.ENDC+"\n\n")
        else:
                print(bcolors.OKBLUE+"This file seems to be OK!"+bcolors.ENDC+"\n\n")

def errorFunc():
        1+1

if __name__ == "__main__":
        main()

