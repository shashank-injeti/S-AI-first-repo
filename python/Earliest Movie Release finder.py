
#______________________________________________________Problem 4: Earliest movie release finder____________________________________________________________________________________


movie_1 , year_1 = input("Enter the first movie's name:") , int(input("Enter Year of release of movie 1:"))
movie_2 , year_2 = input("Enter the second movie's name:") , int(input("Enter Year of release of movie 2:"))
movie_3 , year_3 = input("Enter the third movie's name:") , int(input("Enter Year of release of movie 3:"))
movie_4 , year_4 = input("Enter the fourth movie's name:") , int(input("Enter Year of release of movie 4:"))

if year_1 <= year_2 and year_1 <=  year_3 and year_1 <= year_4:
    if year_1 < year_2 and year_1 <  year_3 and year_1 < year_4:
        movie = movie_1
        year = year_1
    elif year_1 == year_2 and year_1 <  year_3 and year_1 < year_4:
        movie = (movie_1 + " and " + movie_2)
        year = year_1
    elif year_1 < year_2 and year_1 ==  year_3 and year_1 < year_4:
        movie = (movie_1 + " and " + movie_3)
        year = year_1
    elif year_1 < year_2 and year_1 <  year_3 and year_1 == year_4:
            movie = (movie_1 + " and " + movie_4)
            year = year_1
    elif year_1 == year_2 and year_1 ==  year_3 and year_1 < year_4:
            movie = (movie_1 + " and " + movie_2 + " and " + movie_3)
            year = year_1
    elif year_1 == year_2 and year_1 < year_3 and year_1 == year_4:
                movie = (movie_1 + " and " + movie_2 + " and " + movie_4)
                year = year_1
    elif year_1 < year_2 and year_1 ==  year_3 and year_1 == year_4:
                movie = (movie_1 + " and " + movie_3 + " and " + movie_4)
                year = year_1
    elif year_1 == year_2 and year_1 ==  year_3 and year_1 == year_4:
                movie = (movie_1 + " and " + movie_2 + " and " + movie_3 + " and " + movie_4)
                year = year_1

elif year_2 <= year_1 and year_2 <=  year_3 and year_2 <= year_4:
    if year_2 < year_1 and year_2 <  year_3 and year_2 < year_4:
            movie = movie_2
            year = year_2
    elif year_2 == year_1 and year_2 <  year_3 and year_2 < year_4:
            movie = (movie_2 + " and " + movie_1)
            year = year_2
    elif year_2 < year_1 and year_2 ==  year_3 and year_2 < year_4:
            movie = (movie_2 + " and " + movie_3)
            year = year_2
    elif year_2 < year_1 and year_2 <  year_3 and year_2 == year_4:
                movie = (movie_2 + " and " + movie_4)
                year = year_2
    elif year_2 == year_1 and year_2 ==  year_3 and year_2 < year_4:
                movie = (movie_2 + " and " + movie_1 + " and " + movie_3)
                year = year_2
    elif year_2 == year_1 and year_2 < year_3 and year_2 == year_4:
                    movie = (movie_2 + " and " + movie_2 + " and " + movie_4)
                    year = year_2
    elif year_2 < year_1 and year_2 ==  year_3 and year_2 == year_4:
                    movie = (movie_2 + " and " + movie_3 + " and " + movie_4)
                    year = year_2
    elif year_2 == year_2 and year_1 ==  year_3 and year_2 == year_4:
                    movie = (movie_2 + " and " + movie_1 + " and " + movie_3 + " and " + movie_4)
                    year = year_2

elif year_3 <= year_2 and year_3 <=  year_4 and year_3 <= year_4:
    if year_3 < year_2 and year_3 <  year_1 and year_1 < year_4:
            movie = movie_1
            year = year_1
    elif year_3 == year_2 and year_3 <  year_1 and year_3 < year_4:
            movie = (movie_3 + " and " + movie_2)
            year = year_3
    elif year_3 < year_2 and year_3 ==  year_1 and year_3 < year_4:
            movie = (movie_3 + " and " + movie_1)
            year = year_3
    elif year_3 < year_2 and year_3 <  year_1 and year_3 == year_4:
                movie = (movie_3 + " and " + movie_4)
                year = year_3
    elif year_3 == year_2 and year_3 ==  year_1 and year_3 < year_4:
                movie = (movie_3 + " and " + movie_2 + " and " + movie_1)
                year = year_3
    elif year_3 == year_2 and year_3 < year_1 and year_3 == year_4:
                    movie = (movie_3 + " and " + movie_2 + " and " + movie_4)
                    year = year_3
    elif year_3 < year_2 and year_3 ==  year_1 and year_3 == year_4:
                    movie = (movie_3 + " and " + movie_1 + " and " + movie_4)
                    year = year_3
    elif year_3 == year_2 and year_3 ==  year_1 and year_3 == year_4:
                    movie = (movie_3 + " and " + movie_2 + " and " + movie_1 + " and " + movie_4)
                    year = year_3
    

elif year_4 <= year_2 and year_4 <=  year_3 and year_4 <= year_1:
    if year_4 < year_2 and year_4 <  year_3 and year_4 < year_1:
            movie = movie_4
            year = year_4
    elif year_4 == year_2 and year_4 <  year_3 and year_4 < year_1:
            movie = (movie_4 + " and " + movie_2)
            year = year_4
    elif year_4 < year_2 and year_4 ==  year_3 and year_4 < year_1:
            movie = (movie_4 + " and " + movie_3)
            year = year_4
    elif year_4 < year_2 and year_4 <  year_3 and year_4 == year_1:
                movie = (movie_4 + " and " + movie_1)
                year = year_4
    elif year_4 == year_2 and year_4 ==  year_3 and year_4 < year_1:
                movie = (movie_4 + " and " + movie_2 + " and " + movie_3)
                year = year_4
    elif year_4 == year_2 and year_4 < year_3 and year_4 == year_1:
                    movie = (movie_4 + " and " + movie_2 + " and " + movie_1)
                    year = year_4
    elif year_4 < year_2 and year_4 ==  year_3 and year_4 == year_1:
                    movie = (movie_4 + " and " + movie_3 + " and " + movie_1)
                    year = year_4
    elif year_4 == year_2 and year_4 ==  year_3 and year_4 == year_1:
                    movie = (movie_4 + " and " + movie_2 + " and " + movie_3 + " and " + movie_1)
                    year = year_4
    
print("----------------------------------------------------------------------------------------------------------------------")
print(f"The oldest released movie(s) out of the given inputs of movies is/are {movie} and it was released in the year {year}.")
print("----------------------------------------------------------------------------------------------------------------------")
#______________________________________________________________________END OF CODE___________________________________________________________________________________________

