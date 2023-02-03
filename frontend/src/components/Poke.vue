<template>
  <v-card
      class="mx-auto"
      :color="getCor(pokemon.type)"
      dark
      max-width="200"
    >
      <v-card-title>

        <span class="title font-weight-light">{{pokemon.name}}</span>
      </v-card-title>
      
    <div class="d-flex">
          <div>
              <v-card-text class="headline font-weight-bold">
                <v-icon large left >  mdi-heart </v-icon>
                {{ pokemon.hp }}

              </v-card-text>
              <v-card-text class="headline font-weight-bold">
                <v-icon large left >mdi-sword</v-icon>
                {{ pokemon.attack }}
              </v-card-text>
        
              <v-card-text class="headline font-weight-bold">
                <v-icon large left > mdi-shield </v-icon>
                {{ pokemon.armor }}
              </v-card-text>
          </div>

          <div>
            <img :src="getUrl(pokemon.id)" alt="" class="imw">
          </div>
    </div>  

    </v-card>
</template>

<script>
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
      'fogo' : 'red',
      'relampago' : 'yellow',
      'psyco' : 'blue-grey darken-1'
    }
  }),
  methods: {
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
