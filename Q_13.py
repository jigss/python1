try:
    km=0
    print('enter speeed in KM')
    km=raw_input()
    convert_ms= str(float(km)*1000/3600)
    print(str(convert_ms))
except:
    print('please enter number only ')
