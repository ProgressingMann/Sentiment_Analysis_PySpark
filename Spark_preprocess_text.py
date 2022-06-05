from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
import Preprocess_text as pp

spark = SparkSession.builder.master('local').appName('SparkSQLTextClean').getOrCreate()

lines_df = spark.read.json("/Users/mannpurohit/GitHub/Projects/Sentiment_Analysis_Amazon_NLP/reviews_data.json", multiLine=True)

lines_df.show(5)
lines_df.printSchema()

remove_stops_udf = F.udf(pp.remove_stops, StringType())
clean_udf = F.udf(pp.clean_text, StringType())
lemmatize_udf = F.udf(pp.lemmatize, StringType())
check_blanks_udf = F.udf(pp.check_blanks, StringType())

# Remove Stop Words like - 'a', 'is', 'the' as they don't add value.
lines_df = lines_df.select('*')\
                   .withColumn("reviewText", remove_stops_udf(lines_df["reviewText"]))

# Clean the reviews by removing unnecessary characters
lines_df = lines_df.select('*')\
                            .withColumn("reviewText", \
                            clean_udf(lines_df["reviewText"]))

# Perform Lemmatization
lines_df = lines_df.select('*') \
                   .withColumn("reviewText", lemmatize_udf(lines_df["reviewText"]))

# remove blanks
lines_df = lines_df.select('*')\
                             .withColumn("is_blank", check_blanks_udf(lines_df["reviewText"]))
    
# Filter blank lines and remove them
lines_df = lines_df.filter(lines_df["is_blank"] == "False")

lines_df = lines_df.drop("is_blank")

lines_df.show(10)

lines_df.write.json('/Users/mannpurohit/GitHub/Projects/Sentiment_Analysis_Amazon_NLP/')

spark.stop()