data = LOAD './output.txt' USING PigStorage('\n') as (line:chararray);
tokens = foreach data generate flatten(TOKENIZE(line)) As token:chararray;
letter_grp = GROUP tokens by token;
count_letter = FOREACH letter_grp generate group , COUNT(tokens);
dump count_letter;