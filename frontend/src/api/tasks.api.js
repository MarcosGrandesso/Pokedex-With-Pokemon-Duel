import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  getTasks: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/tasks/list")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewTask: (description) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/add", apiHelpers.dataToForm({ description }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  populaPokemon: (params) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/create-pokemon", params )
    })
  },
  getPokemon: () => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/get-pokemon")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },

  getDuels: () => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/get-duelos")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },

  finishDuel: (vencedor) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/finish-duelo", vencedor )
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  createDuel: (pokemon) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/create-duelo", {name:pokemon} )
        // .then((response) => {
        //   return resolve(response.data)
        // })
        // .catch((error) => {
        //   return reject(error)
        // })
    })
  },
  cadastro: (username, senha, senha2) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/register-user", {username:username, senha:senha, senha2:senha2})
    })
  },
}


