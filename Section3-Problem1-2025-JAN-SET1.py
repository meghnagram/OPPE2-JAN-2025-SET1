
berth_types = ["UB","MB","LB", "SU","SL", None]


def calculate_ticket_prices(bookings):
    ticket_prices = {}
    for pnr, booking in bookings.items():
        ticket_prices[pnr] = len(booking['passengers']) * booking['ticket_rate']
    return ticket_prices

def calculate_total_revenue(bookings):
    return sum(
        len(booking['passengers']) * booking['ticket_rate'] 
        for booking in bookings.values()
    )

def count_berth_preferences(bookings):
    berth_count = {berth_type:0 for berth_type in berth_types}
    for booking in bookings.values():
        for _, berth_preference in booking['passengers']:
            berth_count[berth_preference] += 1
    return berth_count

def count_ticket_types(bookings):
    coach_type_count = {}
    for booking in bookings.values():
        coach_type = booking['coach_type']
        coach_type_count[coach_type] = coach_type_count.get(coach_type, 0) + len(booking['passengers'])
    return coach_type_count


def analyze_bookings(bookings, task):
    """
    Analyze the railway ticket bookings based on the given task.
    
    Args:
        bookings (dict): Dictionary with PNR as key and booking details as value.
        task (str): The analysis task to perform.
    
    Returns:
        dict: The result of the requested task.
    """
    
    
    if task == "ticket_prices":
        return calculate_ticket_prices(bookings)
    elif task == "total_revenue":
        return calculate_total_revenue(bookings)
    elif task == "berth_preference_count":
        return count_berth_preferences(bookings)
    elif task == "coach_type_count":
        return count_ticket_types(bookings)

# #Another Method:


# berth_types = ["UB","MB","LB", "SU","SL", None]


# def analyze_bookings(bookings, task):
#     """
#     Analyze the railway ticket bookings based on the given task.
    
#     Args:
#         bookings (dict): Dictionary with PNR as key and booking details as value.
#         task (str): The analysis task to perform.
    
#     Returns:
#         dict: The result of the requested task.
#     """
#     if task=='ticket_prices':
#         d={}
#         # for k in bookings.keys():
#         #     d[k]=0
#         for k in bookings.keys():
#             d[k]=len(bookings[k]["passengers"])*bookings[k]["ticket_rate"]
#         return d
#     if task=="total_revenue":
#         d={}
#         d=analyze_bookings(bookings,"ticket_prices")
#         return sum(d.values())
#     if task=='berth_preference_count':
#         d={}
#         for i in berth_types:
#             d[i]=0
#         for v in bookings.values():
#             c=v["passengers"]
#             for j in c:
#                 if j[1]=='LB':
#                     d['LB'] +=1
#                 if j[1]=='MB':
#                     d['MB'] +=1
#                 if j[1]=='SL':
#                     d['SL'] +=1
#                 if j[1]=='SU':
#                     d['SU'] +=1
#                 if j[1]=='UB':
#                     d['UB'] +=1
#                 if j[1]== None:
#                     d[None] +=1
#         return d
#     if task=='coach_type_count':
#         d={}
#         for v in bookings.values():
#             if v["coach_type"] not in d.keys():
#                 d[v["coach_type"]]=len(v["passengers"])
#             else:
#                 d[v["coach_type"]] += len(v["passengers"])
#         return d

# Railway Ticket Booking Analysis
# You are building a railway ticket analysis system that extracts information about the ticket bookings.

# The booking data is represented as a dictionary of dictionaries, where:

# The key is the PNR number (str) representing the unique booking reference.
# The value is a dictionary containing:
# coach_type (str): Type of the coach ("1AC", "2AC", "3AC", "SL", or "1C").
# ticket_rate (int): Price for one person.
# passengers (list of tuples): A list containing tuples with:
# passenger_name (str): Name of the passenger.
# berth_preference (str): Preference of the berth ("UB", "LB", "MB", "SU", "SL" or None).
# Implement a function analyze_bookings(bookings, task) where task can be one of the following:

# ticket_prices
# Computes a dictionary where the keys are the PNR numbers and the values are the total ticket price for each PNR.
# total_revenue
# Returns the total revenue generated from all ticket bookings.
# berth_preference_count
# Returns the count of passangers in each berth preference as a dictionary with berth_preference as the key and the number of passengers preferred that berth as value.
# Include all the possible berth preference in the output dictionary and let the value be zero if not exists.
# coach_type_count
# Returns a count of passangers in each coach type as a dictionary with coach_type as the key and the number of passengers in that coach as value.
# Only include the coach types that are available in the bookings dictionary in the output.
# Example

# bookings = {
#     "PNR112": {
#         "coach_type": "3AC",
#         "ticket_rate": 900,
#         "passengers": [("Rahul", "UB"), ("Baskar", None)]
#     },
#     "PNR123": {
#         "coach_type": "2AC",
#         "ticket_rate": 1500,
#         "passengers": [("Amit", "LB"), ("Ravi", "UB")]
#     },
#     "PNR456": {
#         "coach_type": "3AC",
#         "ticket_rate": 800,
#         "passengers": [("Priya", "MB"), ("Neha", None)]
#     },
#     "PNR789": {
#         "coach_type": "SL",
#         "ticket_rate": 500,
#         "passengers": [("Vikram", "UB"), ("Kiran", "MB"), ("Surya", "SU")]
#     },
# }

# print(analyze_bookings(bookings, "ticket_prices")) 
# # Output: {'PNR112': 1800, 'PNR123': 3000, 'PNR456': 1600, 'PNR789': 1500}
# print(analyze_bookings(bookings, "total_revenue")) 
# # Output: 7900
# print(analyze_bookings(bookings, 'berth_preference_count')) 
# # Output: {'LB': 1, 'MB': 2, 'SL': 0, 'SU': 1, 'UB': 3, None: 2}
# print(analyze_bookings(bookings, 'coach_type_count')) 
# {'2AC': 2, '3AC': 4, 'SL': 3}
            
        
    
