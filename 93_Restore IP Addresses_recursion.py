"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
合法的ip格式(0~255).(0~255).(0~255).(0~255)
"""
# 参考https://leetcode.com/problems/restore-ip-addresses/discuss/30972/WHO-CAN-BEAT-THIS-CODE改进版本

def restore_ip(ip_str,k,ip_list=[]):

    for i in range(1,4):
        if str(int(ip_str[:i]))==i:
            if int(ip_str[:i])<256:
                restore_ip(ip_str[i:],k-1,ip_list)




if __name__ == '__main__':
    pass


