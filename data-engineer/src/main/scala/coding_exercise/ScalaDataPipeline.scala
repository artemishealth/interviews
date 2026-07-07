package coding_exercise

import com.github.tototoshi.csv.CSVReader

object ScalaDataPipeline {

  def main(args: Array[String]): Unit = {

    // https://github.com/tototoshi/scala-csv
    val reader = CSVReader.open(scala.io.Source.fromResource("file1.csv"))

    val lines: List[List[String]] = reader.all()

    println(lines.take(10))

    //TODO - Goal 1



    //TODO - Goal 2



    //TODO - Goal3



  }
}
