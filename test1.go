package main

import (
	// "log"
	// "net/http"
	"os"

	"github.com/ramsgoli/openweathermap"
)

func main() {
	owm := openweathermap.OpenWeatherMap{API_KEY: os.Getenv("OWM_APP_ID")}
	// http.Handle("/", http.FileServer(http.Dir("web")))

	// err := http.ListenAndServe(":8080", nil)
	// if err != nil {
	// 	log.Fatal(err)
	// 	return
	// }

}
