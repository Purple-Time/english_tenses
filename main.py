


testing = False

if testing:
    sentence = "The dog _ the cat"
    verb = "chase"
    v1 = "chase"
    v2 = "chased"
    v3 = "chased"
    a = "passive"
    p_c = "Perfect"
    ppf = "present"

else:
    print("Hello! Today we will practice using tenses in English!")

    sentence = input("What sentence should we use? (Remove the verb and helping verbs and replace them with an underscore (_)")
    sentence = sentence.replace(".", "")
    verb = input(f"Your sentence is:\n{sentence.replace('_', '________')}\nWhat verb should we use?")
    v1 = input(f"Ok let's use {verb}! Can you give me the v1 form?")
    v2 = input("what about v2?")
    v3 = input("and v3?")
    print("Perfect! So the present tense of your sentence will look like this:")
    print(sentence.replace("_", v1))
    while True:
        a = input("Now let's decide if we want our sentence to be active or passive!").lower()
        if a == "active" or a == "passive":
            break
        else:
            print("Please input either active or passive!")
    if a == "active":
        print("Ok! The sentence is active")
    if a == "passive":
        print("Ok! The sentence is passive")
    while True:
        p_c = input("Now let's decide if we want our sentence to be Continuous [c], Perfect [p], or Perfect Continuous [pc]!").lower()
        if p_c == "c" or p_c == "p" or p_c == "pc":
            break
        else:
            print("Please input p, c, or pc!")
    if p_c == "c":
        p_c = "Continuous"
        print("Ok, the sentence is Continuous!")
    if p_c == "p":
        p_c = "Perfect"
        print("Ok, the sentence is Perfect!")
    if p_c == "pc":
        p_c = "Perfect Continuous"
        print("Ok, the sentence is Perfect Continuous!")
    while True:
        ppf = input("And finally, Let's decide if the sentence should be past, present, or future!").lower()
        if ppf == "past" or ppf == "present" or ppf == "future":
            break
        else:
            print("Please input past, present, or future!")
    if ppf == "past":
        print("Ok, the sentence is past tense!")
    if ppf == "present":
        print("Ok, the sentence is present tense!")
    if ppf == "future":
        print("Ok, the sentence is future tense!")

    print(f"Let's put it all together now! Our current sentence is:\n{sentence.replace('_', '________')}\nand we want to use the verb:\n{v1}\nto make a {ppf}, {p_c}, {a} tense sentence!")
    while True:
        answer_1 = input(f"What is the first thing we should do?\n1. Make it into {ppf} tense\n2. Make it into {p_c} tense\n3. Make it into {a} tense")
        if answer_1 == "1" or answer_1 == "2" or answer_1 == "3":
            break
        else:
            print("Please input 1, 2, or 3!")
    if answer_1 == "3":
        print("Correct! We should always focus on active/passive first!")
    else:
        print("Not quite...We should always focus on active/passive first!")

    print(f"Now let's make the sentence into {a} tense")
    if a == "active":
        print("Good news! We started in active tense, so there is nothing to do!")
    else:
        print("The first step is to find the subject and object of the sentence!")
        while True:
            subject = input("****Add any adjectives to the subject****\nThe subject is: ")
            if subject.lower() in sentence.lower():
                break
            else:
                print("Make sure the spelling matches the subject in your sentence!")
        while True:
            object = input("****Add any adjectives to the object****\nThe object is: ")
            if object.lower() in sentence.lower():
                break
            else:
                print("Make sure the spelling matches the object in your sentence!")
        print("Now let's make the object the new subject!")
        object_temp = object

        if object.lower() == "me":
            object_temp = "i"

        if object.lower() == "him":
            object_temp = "he"

        if object.lower() == "her":
            object_temp = "she"

        if object.lower() == "us":
            object_temp = "we"

        if object.lower() == "them":
            object_temp = "they"

        subject_temp = subject

        if subject.lower() == "i":
            subject_temp = "me"

        if subject.lower() == "he":
            subject_temp = "him"

        if subject.lower() == "she":
            subject_temp = "her"

        if subject.lower() == "we":
            subject_temp = "us"

        if subject.lower() == "they":
            subject_temp = "them"

        s1 = sentence.lower().replace(subject_temp.lower(), "~")
        s2 = s1.lower().replace(object_temp.lower(), "%")
        s3 = s2.replace("~", object_temp)
        print(s3.replace("%", ""))
        print("And then we add the subject to the end of the sentence using by + subject")
        s4 = s3.replace("%", f"by {subject_temp}")
        print(s4)
        print("The last thing we do is add the verb in!")
        print("When making a sentence into passive tense we always add be + v3 so...")
        s5 = s4.replace("_", f"be {v3}")
        while True:
            not_done = input(f"Now the sentence looks like this:\n{s5}\nAre we done?\n1. yes\n2. no")
            if not_done == "1" or not_done == "2":
                break
            else:
                print("Make sure you type 1 or 2!")
        if not_done == 2:
            print("That's right! We still need to make sure that be is in the right form!")
        else:
            print("Not quite! We still need to make sure that be is in the right form!")
        passive_be = input(f"What form should be change to in this sentence?\n{s5}")
        final_passive = s5.replace("be", passive_be, 1)
        print(f"Now we have a passive tense sentence and it looks like this:\n{final_passive}")
