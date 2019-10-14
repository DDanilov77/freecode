//generate RND massive
//choice minimal value from RND massive
//average value from RND massive
//simple Number

package main

import ("fmt"
    "time"
    "math/rand"
)

var (
    i int
    m [1000] int
    srez [] int
    t float64 = 0
    //bminv boolean
    )

const j int = 7

func main() {
    fmt.Println("GoLang :-) Current time is ",time.Now())
    minv:=len(m)
    maxv:=0
    fmt.Println("Len of massive = ",len(m)," : MaxValue : ",minv*7)
    for ii:=0;ii<=len(m)-1;ii++      {
      s1 := rand.NewSource(time.Now().UnixNano())
      r1 := rand.New(s1)
      random1:=r1.Intn(len(m)*7)
      m[ii]=random1
      if minv > m[ii]{
        minv=m[ii]
      }
      if maxv < m[ii]{
        maxv=m[ii]
      }

      //fmt.Println(" Value = ",m[ii]," Min Value = ",minv)
    }
    fmt.Println("Len of massive = ",len(m)," : minv:= ",minv," maxv:= ",maxv)
    small := &m[0]
    for i, _ := range m {
      if *small > m[i] { small = &m[i]}
    }
    fmt.Println("small = ", *small)
    //
    fmt.Println("LAST Return from func_average ",average())
    fmt.Println("Return simple func", simple())
}// end func main

func average() float64{
      //
      for z:=0;z<=len(m)-1;z++ {
        //sx[i]=10
        t+=float64(m[z])
        //fmt.Println(z,"",m[z]," Average ",t/float64(len(m)))
        }//end for
        return t/float64(len(m))
}//end func average

func simple() int {
  var si,x,countdiv,snum int
  for si=1;si<=len(m);si++ {
    countdiv=0
    for x=1;x<=si;x++{
      //fmt.Println("Number(si):= ",si," Circle(x):= ",x," Diving(%):= ", si%x, " Float32 = ", float32(si)/float32(x), ", Int32 = ", si/x)
      if (float32(si)/float32(x)==float32(si/x)) {  countdiv++    }
    }
    if countdiv<=2 {
      snum++
      fmt.Print(" ",si)
    }
  }
  fmt.Println()
  return snum
}
