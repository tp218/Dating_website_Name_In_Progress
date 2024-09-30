import array as arr
import flask

#The i veriable is being used to keep the while loop running in order to test the general functionality
i = 5

#The dictionary of members, one side will be the name, other side will be the member object that coencides with it
member_list = {}

#The class definition for a member
class Member:
  def __init__(self, name):
    self.name = name
    self.bio = ''
    #List of people that this person is interested in, currently thinking of a better name to seperate it from the interests
    self.interest_list = []
    #Interests of the person (Hobbies, things they enjoy)
    self.interests = []
    #People they have already matched with
    self.matches = []

#Will fun after a member adds someone else to their interest list.
#Then this function will search through the interest list of the recently added person
#Then it looks for the given name in that interest list to see if there is a match
def find_match(current_user, recently_added_person):

    #if the person that was just added is in the list of registered members
    if recently_added_person in member_list:

        #Check the interest list of the person that was just added
        for person in member_list[recently_added_person].interest_list:

            #if this entry in the interest_list is the same as the current user that added recently_added_person 
            #then there is a match
            if person == current_user:
                print("You have a match with " + recently_added_person + "!")
                member_list[name].matches.append(recently_added_person)

        #otherwise do nothing
        else:
            print("")
    else:
        print("")

#checks how many items 2 lists have in common
def number_in_common(list1, list2):
    return len(list(set(list1).intersection(list2)))

#This function builds a list of people with similar interests to the current user
def reccomend(name):
    reccomendation_list = {}
    for member in member_list:

        #if this is the current user, then don't check their interest list
        if(member == name):
            print("")
        else:

            #Otherwise find out how many interests this member has in common with our current user
            number = number_in_common(member_list[name].interests, 
                member_list[member].interests)

            #if they share greater than or equal to half of the interests inn our current user's list
            #add them as a reccomendation
            if number >= (len(member_list[name].interests))/2:
                reccomendation_list[member] = number
    return reccomendation_list
        
        
        
            
#Just a placeholder while loop to test how a basic interface of questions would work
while i == 5:
    name = input("What is your name (First and Last) ")

    #If the person "signing in" is not currently a member, add them
    if name not in member_list:
        member_list[name] = Member(name)
    running = True
    while running:

        #Options on what the user can do with their profile
        print("Would you like to")
        print("1. Add a person to your list")
        print("2. Remove from your interest list")
        print("3. Write your Bio")
        print("4. Add and interest")
        print("5. Remove an interest")
        print("6. Get some recomendations")
        print("7. quit")
        answer = input("")

        #Check what option the user selected, and then perform the action they wanted
        if(answer == "1"):
            print("Who would you like to add to your interest list?")
            person_to_add = input("")
            member_list[name].interest_list.append(person_to_add)

            #Check to see if the person they just added had them on their interest_list to see if there's a match
            find_match(name, person_to_add)
            
        elif(answer == "2"):
            print("Who would you like to remove from your interest list?")
            person_to_remove = input("")

            #Check if they are trying to remove someone on their real list
            if person_to_remove in member_list[name][1]:
                member_list[name].interest_list.remove(person_to_remove)
            else:
                print("This person is not in your interest list")
                
        elif(answer == "3"):
            bio = input("Please write your bi0 (500 words max)")

            #make sure the bio wasn't too long
            if len(bio) > 500:
                print("Please write your bio less than 500 words")
            else:
                member_list[name].bio = bio
            
        elif(answer == "4"):
            print("What interest would you like to add?")
            interest = input("")
            member_list[name].interests.append(interest)
            
        elif(answer == "5"):
            print("What interest would you like to remove?")
            interest_to_remove = input("")

            #make sure the interest they are trying to move is in their list
            if interest_to_remove in member_list[name].interests:
                member_list[name].interests.remove(interest_to_remove)
            else:
                print("This interest is not in your interest list")

        elif(answer == "6"):
            reccomendations = reccomend(name)
            print(reccomendations)
                
        elif(answer == "7"):
            running = False

        else:
            "Please enter a valid number"
            
