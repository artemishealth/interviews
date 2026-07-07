package coding_exercise

import org.apache.spark.sql.{DataFrame, SparkSession}

object ScalaSparkDataPipeline {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder().master("local").appName("spark-data-pipeline").getOrCreate()

    val medicalRecords: DataFrame = spark.read.format("csv")
      .option("header", "true")
      .option("inferSchema", "true")
      .load("src/main/resources/file1.csv")

    println(medicalRecords.take(10).mkString("Array(", ", ", ")"))

    //TODO - Goal 1



    //TODO - Goal 2



    //TODO - Goal3



  }
}
