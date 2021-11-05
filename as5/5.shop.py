import csv

PRODUCTS=[]       


def show_menu():
    print('1. Add\n2. Edit\n3. Delete\n4. Show List\n'\
          '5. Search\n6. Buy\n7. Save & Exit\n')

    
def load_data():
    product_dict={}
    
    with open ('database.csv') as f:
        reader=csv.reader(f)
        for line in reader:
            product_dict={'code':line[0],'name':line[1], \
                          'price':line[2],'count':line[3]}
            PRODUCTS.append(product_dict)     

            
def show_list():
    print('Stock :')
    print("{:<9} {:<13} {:<12} {:<11}".format('ID','Name','Price','Count'))
    for product in PRODUCTS:
        print ("{:<9} {:<13} {:<12} {:<11}".format(product['code'],product['name'],\
              product['price'],product['count']))
        
    print('--------------------------------------------------------')




def add():
    print('Adding Products ... ')
    new_product={'code':input('Product Code : '),'name':input('Product Name : '),
                 'price':input('Product Price : '),'count':input('Product Count : ')}
    ex=0
    for product in PRODUCTS:
        if new_product['code'] == product['code'] or new_product['name'] == product['name']  :
            ex=1
            print('Product With This Code or Name is Already Exists! You Can Edit It')
            break
    if ex==0 :
        PRODUCTS.append(new_product)
        print('--- Product Added ---')
    

                 
def edit():
    print('Editing Products ...')
    edit_name=input('Product Name : ')
    in_stock=False
    index=0
    for product in PRODUCTS:
        if product['name']==edit_name :
            in_stock=True
            break
        else:
            index+=1
    if in_stock:
        while True :
            choice=int(input('Which Part of Product You Want to Edit ?\n1. Code\n2. Name\n3. Price\n4. Count\n5. Quit Edit\n'))
            if choice==1:
                new_code=input('New Code : ')
                PRODUCTS[index]['code']=new_code

            elif choice==2:
                new_name=input('New Name : ')
                PRODUCTS[index]['name']=new_name
    
            
            elif choice==3:
                new_price=input('New Price : ')
                PRODUCTS[index]['price']=new_price

            elif choice==4:
                new_count=input('New Count : ')
                PRODUCTS[index]['count']=new_count

            elif choice==5:
                print('--- Edit Saved ---')
                break
            else :
                print('Choose Between 1 and 5')
    else:
            print('Product is Out of Stock! You Can Add It.')
                    
        
    

def delete():
    print('Deleting Product ...')
    delete_name=input('Product Name : ')
    for i in range(0,len(PRODUCTS)):
        if PRODUCTS[i]['name']==delete_name:
            del PRODUCTS[i]
            print('--- Product Deleted ---')
            break
    else :
        print('Product is Out of Stock!')

            
               
def search():
    print('Searching Product ... ')
    search_name=input('Product Name : ')
    for i in range(0,len(PRODUCTS)):
        if PRODUCTS[i]['name']==search_name:
            print('Product Found!')
            for k,v in PRODUCTS[i].items():
                print(k.upper(),' : ',v,end='  |  ')
            print()
            break
    else :
        print('Product is Out of Stock!')


        
def buy():
    print('Shopping ...')
    basket=[]
    quan=[]
    final_cost=0
    while True:
        choice = int(input('1. Buy Product\n2. Show Basket\n3. Quit\nChioce : '))
        if choice==1:
            buy_name=input('Product Name : ')
            for product in PRODUCTS:
                if product['name']==buy_name:
                    qty=-1
                    while qty<=0:
                        qty=int(input('Quantity : '))
                    if qty>int(product['count']):
                        print('Only ',product['count'],' Left in Stock!')
                        break
                    else:
                        quan.append(qty)
                        basket.append({'code':product['code'],'name':product['name'], \
                                       'price':product['price'],'count':product['count']})
                        product['count']=str(int(product['count'])-qty)
                        final_cost+=int(product['price'])*qty
                        break
            else :
                print('Sorry! Product is Out of Stock.')
                        
                        
        elif choice==2:
            
            print("{:<9} {:<13} {:<12} {:<11}".format('ID','Name','Price','Quantity'))
            if final_cost==0:
                print('Your Basket is Empty!')
            i=0
            for product in basket :
                print ("{:<9} {:<13} {:<12} {:<11}".format(product['code'],product['name'],\
                       product['price'],quan[i]))
                i+=1
            print('Final Cost : ',final_cost)
        
        elif choice==3:
            print('--- End Shopping ---')
            break
        
        else :
            print('Choose Between 1 and 3')

def save():
    with open ('database.csv','w',newline='') as fd:
        writer=csv.DictWriter(fd,fieldnames=['code','name','price','count'])
        for product in PRODUCTS:
            writer.writerow(product)
    print('Successfully Saved\nGood Luck')


    
load_data()

while True:
    #break
    show_menu()
    sel=int(input('Enter Your Choice : '))
    
    if sel==1:
        add()
    
    elif sel==2:
        edit()
        
    elif sel==3:
        delete()
        
    elif sel==4:
        show_list()
        
    elif sel==5:
        search()
        
    elif sel==6:
        buy()
        
    elif sel==7:
        save()
        break
    else:
        print('Choose Between 1 and 7')
    
    
