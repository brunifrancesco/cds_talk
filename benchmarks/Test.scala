import java.io.File
import com.github.tototoshi.csv._


 object Test {
  def main(args: Array[String]) {
    println("Evaluating...")
    evaluateResult(streamGen, List(10, 100, 1000, 10000, 100000, 1000000), "lazy")
    evaluateResult(filterStrict, List(10, 100, 1000, 10000, 100000, 1000000), "filter_strict")
    evaluateResult(factorial, List(10, 20, 40), "factorial")
    evaluateResult(factorial_tc, List(10, 20, 40), "factorial_tc")
    println("Done")
   }


def streamGen(size: Int, acc: Int) : Int ={
  (1 to size).toStream
  1
}


def filterStrict(size: Int, acc: Int) : Int ={
  (1 to size).toStream.filter(x => x % 2 == 0).toList
  1
}

def factorial(size: Int, acc: Int) : Int = {
    if(size == 0){
      return 1
    }
    return size * factorial(size-1, acc)
}

def factorial_tc(size: Int, acc: Int) : Int = {

    if(size == 0){
      return 1
    }
    return factorial_tc(size-1, acc*size)
}

def evaluateResult(func: (Int, Int) => Int, sizes: List[Int], funcName: String)= {
    val writer = CSVWriter.open("scala.csv", append = true)
    sizes.foreach  { size =>
      (1 to 10).foreach{ it =>
        val start = java.lang.System.nanoTime()
        func(size, 1)
        val end = java.lang.System.nanoTime() - start
        writer.writeRow(List("scala", funcName, it, size, end))
      }
    }
   }

}
