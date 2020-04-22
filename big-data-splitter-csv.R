# R method to make csvs based on Rows. Did rows because approx ` 60000 rows are 23 MB which are close to the max
# size allowed on github upload. 

library(tidyverse)

bigdf_data <- readr::read_csv("xyz.csv") #Read in the original csv file

#break the large CSV so RAM and Rstudio doesn't crash

groups <- (split(bigdf_data, (seq(nrow(bigdf_data))-1) %/% 60000)) #here I want 60000 rows per file until last row is reached

for (i in seq_along(groups)) {
  write.csv(groups[[i]], paste0("bigdf_data_output_file", i, ".csv")) #iterate and write file
}

# all the files will be in the current directory. 
