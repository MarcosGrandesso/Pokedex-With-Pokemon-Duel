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
      {id:6, title:'charizard', type: 'fogo', hp:134, armor : 200, attack: 30},
      {id:25,title:'pikachuloco', type: 'relampago', hp:14, armor : 4200, attack: 430},
      {id:150, title:'mewtwo', type: 'psyco', hp:400, armor : 2200, attack: 340},
      {id:7,title:'squirtle', type: 'agua', hp:14, armor : 4200, attack: 430},
      {id:2, title:'mewtwo', type: 'psyco', hp:400, armor : 2200, attack: 340},
      // {id:51,name:'pikachuloco', type: 'relampago', hp:14, armor : 4200, attack: 430},
    ]
      return later(result)
  },
  
  async getDuelos(user=1) {
    const result = [

      { id : 1,
        usuario : {name: 'marquinho duelista', pokemons:5, foto: 'https://avatars.githubusercontent.com/u/104371113?s=400&u=35cfd90eec5e2802cd5512f456cd7f1806a37fdf&v=4'},
        vencedor : null,
        pokemon : {id:6, name:'charizard', type: 'fogo', hp:1, armor : 1, attack: 30}
      },
      { id : 1,
        usuario : {name: 'Tony Lampkins',pokemons:5, foto: 'https://avatars.githubusercontent.com/u/104371113?s=400&u=35cfd90eec5e2802cd5512f456cd7f1806a37fdf&v=4'},
        vencedor : null,
        pokemon : {id:1, name:'charizard', type: 'fogo', hp:134, armor : 200, attack: 30}
      },
      { id : 1,
        usuario : {name: 'duelista', foto: 'https://avatars.githubusercontent.com/u/104371113?s=400&u=35cfd90eec5e2802cd5512f456cd7f1806a37fdf&v=4'},
        vencedor : null,
        pokemon : {id:6, name:'charizard', type: 'fogo', hp:134, armor : 200, attack: 30}
      },
      
      // {id:51,name:'pikachuloco', type: 'relampago', hp:14, armor : 4200, attack: 430},
    ]
      return later(result)
  }
}

export default {
  mocked_api
}