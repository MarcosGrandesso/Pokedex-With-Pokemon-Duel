<template>
  <v-card
      class="mx-auto"
      :color="getCor(pokemon.fields.type)"
      dark
      max-width="200"
    >
      <v-card-title>

        <h3 class="title font-weight-bold">{{pokemon.fields.title}}</h3>
      </v-card-title>
      
    <div class="d-flex">
          <div>
              <v-card-text class="headline font-weight-bold">
                <v-icon large left >  mdi-heart </v-icon>
                {{ pokemon.fields.hp }}

              </v-card-text>
              <v-card-text class="headline font-weight-bold">
                <v-icon large left >mdi-sword</v-icon>
                {{ pokemon.fields.attack }}
              </v-card-text>
        
              <v-card-text class="headline font-weight-bold" >
                <v-icon large left > mdi-shield </v-icon>
                {{ pokemon.fields.armor }}
              </v-card-text>
          </div>

          <div>
            <img :src="pokemon.fields.img_url" alt="" class="imw">
          </div>
    </div>  

    </v-card>
</template>

<script>

import api from '@/api/tasks.api'

export default {
  name: "TasksModel",
  props: {
    pokemon: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({
    cor: '',
    mapColor: {
      'fire' : 'red',
      'electric' : 'yellow',
      'psychic' : 'grey lighten-3',
      'water' : 'blue lighten-2',
      'poison' : 'light-green accent-2',
      'grass' : 'green darken-4',
      'bug' : 'brown lighten-2',
      'fairy' : 'pink accent-1',
      'rock' : 'blue-grey darken-2',
      'fighting': 'amber darken-4',
      'ghost': 'purple darken-4',
      'normal' : 'red accent-4',
      'ground' : 'blue-grey darken-4',
      'dragon' : 'teal darken-1'
    },
    // pokename: ["Bulbasaur"]
    // pokename: ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidorina","Nidoqueen","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
  }),
  methods: {
    poppk() {
      api.getPokemon()
      // let pokedavez = {}
      // for (let i of this.pokename) {
        // fetch(`https://pokeapi.co/api/v2/pokemon/${i.toLowerCase()}`).then((res)=> {res.json().then((pokemon)=> {
        // pokedavez = pokemon
        // pokedavez.imagem = this.getUrl(pokedavez.id)
        // console.log(pokedavez)
        // let poke =  {id: pokedavez.id,type: pokedavez.types[0].type.name, title: pokedavez.name, hp: pokedavez.stats[0].base_stat, attack: pokedavez.stats[1].base_stat, armor:  pokedavez.stats[2].base_stat, img_url: pokedavez.imagem}
        // console.log(a)
      // })
    // })
      },
    getCor(typo) {
      return this.mapColor[typo]
    },
    getUrl(id) {
      return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`
    }
  },
  watch: {
     pokemon() {
      console.log(this.mapColor[pokemon.type])
       this.cor = this.mapColor[pokemon.type]
     },
  }
}
</script>

<style scoped>
.imw {
  height: 150px;
}

.v-card-text {
  padding: 0;
  padding-left: 1rem;
  padding-bottom: 0.5rem;
}
</style>
