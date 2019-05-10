"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
合法的ip格式(0~255).(0~255).(0~255).(0~255)
"""
# 参考https://leetcode.com/problems/restore-ip-addresses/discuss/30972/WHO-CAN-BEAT-THIS-CODE改进版本

def restore_ip(ip_str):
    ip_list=[]
    for i1 in range(1,4):
        for i2 in range(1,4):
            for i3 in range(1,4):
                for i4 in range(1,4):
                    if i1+i2+i3+i4==len(ip_str):
                        str1=int(ip_str[:i1])
                        str2=int(ip_str[i1:i1+i2])
                        str3=int(ip_str[i1+i2:i1+i2+i3])
                        str4=int(ip_str[i1+i2+i3:])
                        if len(str(str1)+str(str2)+str(str3)+str(str4))==len(ip_str):
                            if str1<256 and str2<256 and str3<256 and str4<256:
                                ip_list.append(str(str1)+'.'+str(str2)+'.'+str(str3)+'.'+str(str4))
    print(ip_list)
    return ip_list


if __name__ == '__main__':
    restore_ip("0000")



