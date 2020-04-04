# Q10
cat popular-names.txt | wc -l

# Q11
cat ./popular-names.txt | sed -e 's/\t/ /g'

# Q12
cat popular-names.txt | cut -f 1,2 -d \t