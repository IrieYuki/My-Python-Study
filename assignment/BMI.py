def caculate_bmi (weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    
    :param weight: Weight in kilograms
    :param height: Height in meters

    :returns: The calculated BMI
    """

    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return bmi

BMI = caculate_bmi(float(input("请输入体重（公斤）：")), float(input("请输入身高（米）：")))
print (BMI)

if BMI < 18.5:
    print("体重过轻")
elif 18.5 <= BMI < 24:
    print("体重正常")
elif 24 <= BMI < 28:
    print("体重过重")