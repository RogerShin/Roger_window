def BMI():
    try:
        person_hight_cm = int(input("請輸入您的身高："))
        person_weight = int(input("請輸入您的體重："))
    except ValueError:
        raise("錯誤,請輸入數字!")
    else:
        m = person_hight_cm/100
        personBMI = person_weight/pow(m, 2)

        # 理想體重算法
        best_weight = pow(m, 2) * 22

        if  personBMI < 18.5:
            increase = best_weight - person_weight
            weigh_info = f"體重過輕!"
            advice = f" 建議增重{increase:.2f}公斤, 為您的理想體重！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice
        elif personBMI >= 18.5 and personBMI < 24:
            weigh_info = f"恭喜！「健康體重」"
            advice = f"請繼續保持！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice
        elif personBMI >= 24 and personBMI < 27:
            reduce_weight = person_weight - best_weight
            weigh_info = f"「過重」，小心囉！ "
            advice = f"建議減少{reduce_weight:.2f}公斤, 為理想體重！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice
        elif personBMI >= 27 and personBMI < 30:
            reduce_weight = person_weight - best_weight
            weigh_info = f"「輕度肥胖」了，要小心囉！ "
            advice = f"建議減少{reduce_weight:.2f}公斤, 為理想體重！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice
        elif personBMI >= 30 and personBMI < 35:
            reduce_weight = person_weight - best_weight
            weigh_info = f"啊～「中度肥胖」，需要注意囉!"
            advice = f"建議減少{reduce_weight:.2f}公斤, 為理想體重！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice
        else:
            reduce_weight = person_weight - best_weight
            weigh_info = f"天啊～「重度肥胖」！"
            advice = f"建議減少{reduce_weight:.2f}公斤, 為理想體重！"
            return person_hight_cm, person_weight, personBMI, weigh_info, advice

def dict_info() -> list[dict]:
    
    name = input("請輸入姓名：")
    if name.isspace() is True or len(name) == 0:
        return "不能為空白！"
    elif name.isdigit():
        return "不能為數字"
    else:
        hight_cm, weight, personBMI, weigh_info, advice = BMI()
        info = {}
        info['name'] = name
        info['hight_cm'] = hight_cm
        info['weight'] = weight
        info['BMI'] = f"{personBMI:.2f}"
        info['weigh_info'] = weigh_info
        info['advice'] = advice
        lis:list[dict]=[info]
        return lis