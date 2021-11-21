#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Author : Neel V Zadafiya (1115533)

#Import required libraries
import pytholog as pl


# In[2]:


# Define class
class SimpsonFamily:
    
    # Constructor function
    def __init__(self):
        
        # Set knowledge base
        self.family_base = pl.KnowledgeBase("simpson_family")

        # Define predicates and clauses
        self.family_base([
            
            # Father relations : X is father of Y
             "father(abe,herb)",
             "father(abe,homer)",
             "father(clancy,marge)",
             "father(clancy,patty)",
             "father(clancy,selma)",
             "father(homer,bart)",
             "father(homer,lisa)",
             "father(homer,maggie)",
             
            # Mother relations : X is mother of Y
             "mother(mona,herb)",
             "mother(mona,homer)",
             "mother(jacqueline,marge)",
             "mother(jacqueline,patty)",
             "mother(jacqueline,selma)",
             "mother(marge,bart)",
             "mother(marge,lisa)",
             "mother(marge,maggie)",
             "mother(selma,ling)",
             
            # Males : X is male
             "male(abe)",
             "male(clancy)",
             "male(herb)",
             "male(homer)",
             "male(bart)",
             
            # Females : X is female
             "female(mona)",
             "female(jacqueline)",
             "female(marge)",
             "female(patty)",
             "female(selma)",
             "female(lisa)",
             "female(maggie)",
             "female(ling)",
             
            # 1. Parent clause : X is parent of Y
            # X is either mother of father of Y
             "parent(X,Y) :- father(X,Y)",
             "parent(X,Y) :- mother(X,Y)",
             
            # 2. Brother caluse : X is brother of Y
            # X and Y has same father M and same mother N
            # X is male and not same as Y
             "brother(X,Y) :- father(M,X), father(M,Y), mother(N,X), mother(N,Y), male(X), neq(X,Y)",
            
            # 3. Sister caluse : X is sister of Y
            # X and Y has same father M and same mother N
            # X is female and not same as Y
             "sister(X,Y) :- father(M,X), father(M,Y), mother(N,X), mother(N,Y), female(X), neq(X,Y)",
             
            # 6. Grand parent clause : X is grand parent of Y
            # X is parent of M and M is parent of Y
             "grand_parent(X,Y) :- parent(X,M), parent(M,Y)",
            
            # 4. Grand father clause: X is grand father of Y
            # X is male and grand parent of Y
             "grand_father(X,Y) :- grand_parent(X,Y), male(X)",
            
            # 5. Grand mother clause: X is grand father of Y
            # X is female and grand parent of Y
             "grand_mother(X,Y) :- grand_parent(X,Y), female(X)",
             
            # 7. Uncle clause: X is uncle of Y
            # Parent M of Y is brother of X
             "uncle(X,Y) :- parent(M,Y), brother(X,M)",
            
            # 8. Aunt clause: X is aunt of Y
            # Parent M of Y is sister of X
             "aunt(X,Y) :- parent(M,Y), sister(X,M)",
             
            # 9.1 Nephew clause: X is nephew of Y
            # Y is either uncle or aunt of X and X is male
             "nephew(X,Y) :- uncle(Y,X), male(X)",
             "nephew(X,Y) :- aunt(Y,X), male(X)",
             
            # 9.2 Niece clause: X is niece of Y
            # Y is either uncle or aunt of X and X is female
             "niece(X,Y) :- uncle(Y,X), female(X)",
             "niece(X,Y) :- aunt(Y,X), female(X)",
             
            # 9.3 Sibling clause: X is sibling of Y
            # X is either brother of sister of Y
             "sibling(X,Y) :- brother(X,Y)",
             "sibling(X,Y) :- sister(X,Y)"
             
            ])
        
    # Test function to display relations between two people
    # This function takes three parameters, First is relation followed by person1 and person2
    def test_relation(self,relation,person1,person2):
        
        # Display title
        print("Testing relation: "+relation+" between "+person1+" and "+person2)
        print()
        
        # Display notmal output of query
        print("Is "+person1+" "+relation+" of "+person2+" ?")
        answer = self.family_base.query(pl.Expr(relation+"("+person1+","+person2+")"))
        print(answer[0])
        print()
        
        # Display output of query with swapped arguments
        print("Is "+person2+" "+relation+" of "+person1+" ?")
        answer = self.family_base.query(pl.Expr(relation+"("+person2+","+person1+")"))
        print(answer[0])
        print()
        
        # Display who is related to person 1
        print("Whose "+relation+" is "+person1+"?")
        answer = self.family_base.query(pl.Expr(relation+"("+person1+",Who)"))
        if answer[0] != "No":
            for i in answer:
                print(i['Who'],end=", ")
            print()
        else:
            print("No one's")
        print()
        
        # Display person 1 is realated to whom
        print("Who is(are) "+relation+"(s) of "+person2+" ?")
        answer = self.family_base.query(pl.Expr(relation+"(Who,"+person2+")"))
        if answer[0] != "No":
            for i in answer:
                print(i['Who'],end=", ")
            print()
        else:
            print("No one")
        print()
        print()
        
# End of class SimpsonFamily


# In[3]:


# Get object of defined class
sf = SimpsonFamily()


# In[4]:


# Check parent relation between homer and bart
sf.test_relation("parent","homer","bart")


# In[5]:


# Check brother relation between bart and lisa
sf.test_relation("brother","bart","lisa")


# In[6]:


# Check sister relation between lisa and bart
sf.test_relation("sister","lisa","bart")


# In[7]:


# Check grand father relation between abe and bart
sf.test_relation("grand_father","abe","bart")


# In[8]:


# Check grand mother relation between mona and bart
sf.test_relation("grand_mother","mona","bart")


# In[9]:


# Check grand parent relation between abe and bart
sf.test_relation("grand_parent","abe","bart")


# In[10]:


# Check uncle relation between herb and bart
sf.test_relation("uncle","herb","bart")


# In[11]:


# Check aunt relation between patty and bart
sf.test_relation("aunt","patty","bart")


# In[12]:


# Check nephew relation between bart and herb
sf.test_relation("nephew","bart","herb")


# In[13]:


# Check niece relation between lisa and herb
sf.test_relation("niece","lisa","herb")


# In[14]:


# Check sibling relation between bart and lisa
sf.test_relation("sibling","bart","lisa")


# In[ ]:




