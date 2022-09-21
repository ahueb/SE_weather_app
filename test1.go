package main

import (
	"fmt"
	"log"
	"net/http"
)

func sayHi(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi")
}

func main() {
	http.Handle("/", http.FileServer(http.Dir("web")))

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
		return
	}
}
