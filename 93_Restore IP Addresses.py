"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
合法的ip格式(0~255).(0~255).(0~255).(0~255)
"""
def restore_ip(ip_str):
    ip_list=list(ip_str)
    valid_list=[]
    for i1 in range(1,4):
        if not ip_list[:i1] :
            break
        first=int(''.join(ip_list[:i1]))
        if ''.join(ip_list[:i1]).startswith('0') and len(''.join(ip_list[:i1]))>1:
            break
        if first<0 or first>255:
            break
        for i2 in range(1,4):
            if not ip_list[i1:i1+i2] :
                break
            sendcond=int(''.join(ip_list[i1:i1+i2]))
            if ''.join(ip_list[i1:i1+i2]).startswith('0') and len(''.join(ip_list[i1:i1+i2])) > 1:
                break
            if sendcond < 0 or sendcond > 255:
                break
            for i3 in range(1,4):
                if not ip_list[i1+i2:i1+i2+i3]:
                    break
                third=int(''.join(ip_list[i1+i2:i1+i2+i3]))
                if ''.join(ip_list[i1+i2:i1+i2+i3]).startswith('0') and len(''.join(ip_list[i1+i2:i1+i2+i3])) > 1:
                    break
                if third < 0 or third > 255 :
                    break
                if not ip_list[i1+i2+i3:] or len(ip_list[i1+i2+i3:])>3:
                    continue
                last=int(''.join(ip_list[i1+i2+i3:]))
                if last < 0 or last > 255:
                    continue
                if ''.join(ip_list[i1+i2+i3:]).startswith('0') and len(''.join(ip_list[i1+i2+i3:])) > 1:
                    continue
                temp_list=[]
                temp_list.append(''.join(ip_list[:i1]))
                temp_list.append(''.join(ip_list[i1:i1+i2]))
                temp_list.append(''.join(ip_list[i1+i2:i1+i2+i3]))
                temp_list.append(''.join(ip_list[i1+i2+i3:]))
                valid_ip='.'.join(temp_list)
                valid_list.append(valid_ip)
    print(valid_list)
    return valid_list
if __name__ == '__main__':
    restore_ip("101023")



