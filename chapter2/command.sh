# Q10
cat popular-names.txt | wc -l

# Q11
cat ./popular-names.txt | sed -e 's/\t/ /g'

# Q12
cat popular-names.txt | cut -f 1,2 -d \t

# Q13
paste col1.txt col2.txt

# Q14
head -n 3 popular-names.txt

# Q15
tail -n 3 popular-names.txt

# Q16
N=3; split popular-names.txt -n l/$N -d popular-names --additional-suffix=.txt

# Q17
sort popular-names.txt | cut -f 1 -d $'\t' | uniq

# Q18
sort -k 3 -t $'\t' -r -n popular-names.txt

# Q19
sort popular-names.txt | cut -f 1 -d $'\t' | uniq -c | sort -n