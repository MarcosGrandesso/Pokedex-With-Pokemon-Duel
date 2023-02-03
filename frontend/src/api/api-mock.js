function later(result) {
  return new Promise(function(resolve) {
    setTimeout(() => {
      resolve(result)
    }, 1000)
  })
}

const mocked_api = {


  async getPokes(user=1) {
    const result = [
      {id:6, name:'charizard', type: 'fogo', hp:134, armor : 200, attack: 30},
      {id:25,name:'pikachuloco', type: 'relampago', hp:14, armor : 4200, attack: 430},
      {id:150, name:'mewtwo', type: 'psyco', hp:400, armor : 2200, attack: 340},
      {id:7,name:'squirtle', type: 'agua', hp:14, armor : 4200, attack: 430},
      {id:2, name:'mewtwo', type: 'psyco', hp:400, armor : 2200, attack: 340},
      // {id:51,name:'pikachuloco', type: 'relampago', hp:14, armor : 4200, attack: 430},
    ]
      return later(result)
  }
}

export default {
  mocked_api
}