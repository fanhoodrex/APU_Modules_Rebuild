import time

def menu():
    """function for displaying the menu"""
    print("Hello, This is the menu of UTOMOBILE PARTS INVENTORY MANAGEMENT SYSTEM")
    time.sleep(1)
    print("""
    1.Parts Inventory Creation in Warehouses
    2.Parts Inventory Update
    3.Parts Inventory Tracking
    4.Searching Functionalities
    5.Exit
    """)
    return None

def AssemblySections_CodeList():
    """function for creating assembly list containing assembly code """
    list_assembly = [] # initialize assembly_sections variable in local scope
    while True: # Loop validation that input numebr large must be at least three
        num_sections = int(input("How many assembly sections are there in total?:"))
        if num_sections < 3:
            print("Sorry, there should be at least 3 assembly sections in each warehouse")
            time.sleep(1)
            continue
        else:
            for num in range(num_sections):
                section = input(f"What is the {num+1} assembly section?:")
                list_assembly.append(section) # append individual section input to assembly sections list
            break
    return list_assembly

def Warehouses_CodeList():
    """function for creating list containing warehouse code"""
    list_warehouse = [] # initialize the empty list for warehouse code in local scope
    while True: # While Loop to enter the warehouses
        num_warehouses = int(input("How many warehouses are there in total?:"))
        if num_warehouses >= 3: # at least three warehouses
            for num in range(num_warehouses):
                warehouse = input(f"What is the {num+1} warehouse?:")
                list_warehouse.append(warehouse) # append individual section input to assembly sections list
            break
        else:
            print("Sorry, there should be at least 3 warehouses")
            time.sleep(1)
            continue
    time.sleep(1)
    print(f"Successfully create all warehouses:{list_warehouse}")
    return list_warehouse

def Part():
    """Function for creating individual part element"""
    part_details = {} # initialize part variable in local scope
    warehouse_value = [] # initialize warehouse_value variable in local scope
    warehouse_value = [] # initialize warehouse_value variable in local scope

    part_details['id'] = input("What is the unique id should be given for this parts?: ") # assign the unique id key/value for part dict
    part_details['initial_quantity'] = int(input("How many is the initial quantity for this part?:")) # assign the initial quantity key/value for part dict
    part_details['supplier'] = input("Enter one supplier only for this part:") # assign the supplier key/value for part dict
    suppliersList.append(part_details["supplier"])

    while True: # while loop for selecting those warehouses with which the each part are supplied 
        ware_input = input("What warehouses is this part under? Enter 0 to finish:")
        if ware_input in Warehouses_CodeList"
            warehouse_value.append(ware_input)
        else:
            print("Pls enter valid warehouses:")
            continue
            time.sleep(1)
    part_details['warehouse'] = warehouse_value # assign the warehouse list as value to the warehosue key in part dict

    while True: # while loop for selecting those assembly sections with which the each part are supplied 
        print(AssemblySections_CodeList)
        section_input = input("What assambly sections is this part provided to?:")
        if section_input == str(0):
            break
        else:
            warehouse_value.append(section_input)
            continue
            time.sleep(1)
    part_details['assembly section'] = warehouse_value # assign the assembly sections as value to the assembly section key in part dict

    time.sleep(1)
    print(f"""Successfully created a single part, shown as below
-----------------------------------------------------------------
    {part_details}""") # use f-string with triple quotation
    return part_details