fruits={'apple','orange','pear','grape'} #集合是无序的
counts=[10,20,30,40]
for f,c in zip(fruits,counts):
    match f,c:
        case'apple',10:
            print('10个苹果')
        case'orange',20:
            print('20个橘子')
        case'pear',30:
            print('30个梨子')
        case'grape',40:
            print('40串葡萄')