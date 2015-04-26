(ns clj.core)

(defn is-valid-isbn13?
  [isbn]
  (let [isbn-digits (map #(Integer/parseInt (str %)) (seq isbn))
        isbn-numbers (take 12 isbn-digits)

        actual-check-digit (last isbn-digits)

        even-nums (take-nth 2 isbn-numbers)
        even-nums-summed (reduce + 0 even-nums)

        odd-nums (take-nth 2 (rest isbn-numbers))
        odd-nums-thriced (map #(* % 3) odd-nums)
        odd-nums-thriced-summed (reduce + 0 odd-nums-thriced)

        total-sum (+ odd-nums-thriced-summed even-nums-summed)
        expected-check-digit (mod (- 10 (mod total-sum 10)) 10)]

    (= actual-check-digit expected-check-digit)))

(defn -main 
  [isbn]
  (if (not= (.length isbn) 13)
    (do
      (println "ERROR: ISBN should be 13 digits long")
      (System/exit 1)))
  (if (is-valid-isbn13? isbn)
    (println "Valid")
    (do
      (println "ERROR: Invalid ISBN")
      (System/exit 2))))

