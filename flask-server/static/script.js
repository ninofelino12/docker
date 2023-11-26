document.addEventListener("DOMContentLoaded", main)

function main() {
  const binary = document.querySelector("input")
  const errMsg = document.querySelector(".err")
  const btn = document.querySelector("button")
  const decimal = document.querySelector("textarea")

  btn.setAttribute("disabled", "true")
  binary.addEventListener("input", validate)
  btn.addEventListener("click", convert)

  function validate(e) {
    const value = e.target.value
    const regex = /^[0-1]+$/g

    if (value.length < 1) {
      errMsg.textContent = "not allowed empty"
      btn.setAttribute("disabled", "true")
      return
    }
    if (regex.test(value) === false) {
      errMsg.textContent = "not binary number"
      btn.setAttribute("disabled", "true")
      return
    }
    errMsg.textContent = ""
    btn.removeAttribute("disabled")
  }

  function convert() {
    const value = binary.value

    const result = value
      .split("")
      .reverse()
      .reduce((acc, curr, index) => {
        return acc + parseInt(curr) * Math.pow(2, index)
      }, 0)

    decimal.textContent = result
  }
}
