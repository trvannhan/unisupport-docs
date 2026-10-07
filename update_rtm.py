import os

def update_rtm():
    path = 'd:/docs/06-acceptance/traceability-matrix.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_st5 = "| **REQ-STU-05** | Bổ sung thông tin & phản hồi theo yêu cầu nhân viên | M01-student-portal | WF-03 | TS-STU-04 | Chờ UAT |"
    old_st6 = "| **REQ-STU-06** | Xem kết quả & đánh giá mức độ hài lòng | M01-student-portal | WF-06 | TS-STU-05 | Chờ UAT |"
    
    new_st5 = "| **REQ-STU-05** | Bổ sung thông tin & phản hồi, xem kết quả và đánh giá | M01-student-portal | WF-03, WF-06 | TS-STU-04 | Chờ UAT |"
    
    if old_st5 in content and old_st6 in content:
        content = content.replace(old_st5 + "\n" + old_st6, new_st5)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
update_rtm()
print("RTM updated")
