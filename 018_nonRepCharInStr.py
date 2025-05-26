"""6.find the first non-repeating character in a string e.g "Test" should outptut 'e'"""

st = "kakrkayi"

for i in st.lower():
    count = 0
    for j in st.lower():
        if i == j:
            count += 1
    if count == 1:
        break
print(i)
    
        
