<template>
  <v-container class="fill-height mxw">
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-card>
          <v-card-title class="headline"> Duelos Disponiveis </v-card-title>
        </v-card>
      </v-col>

      <!-- <v-col cols="12">
        <Poke-form :form-label="'Nova Tarefa'" @new-task="addNewTask" />
      </v-col> -->
<div class="d-flex maxw">
  <div v-for="item in items" :key="item.id">
    <duel-card :duels="item" @open-duel-modal="openModal"/>
  </div>
</div>
    </v-row>

    <v-dialog
        v-model="dialog2"
        max-width="500px"
      >
        <v-card>
          <v-card-title>
            Hora Da Batalha
          </v-card-title>
          <v-card-text>
            <v-select v-if="!pokeToDuel"
              v-model="pokeToDuel"
              :items="select"
              label="Escolha Seu Pokemon"
              item-value="text"
            ></v-select>
            <div v-else class="d-flex gp">
              <img :src="getUrl(pokemon[0].id)" alt="" class="imw">
              <h1 class="margin">X</h1>
              <img v-if="!vaiLutar" src="https://cdn-icons-png.flaticon.com/512/57/57108.png" alt="" class="imw">
              <img v-else :src="getUrl(adversario.id)" alt="" class="imw">

            
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn
              color="#952175"
              text
              @click="fugir"
            >
              Fugir
            </v-btn>
            <v-btn
              color="#952175"
              text
              @click="initLuta(this.pokemon[0], this.adversario)"
            >
              Lutar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import mock from "@/api/api-mock"
import DuelCard from "@/components/DuelCard.vue"
import PokeForm from "@/components/PokeForm.vue"
// import DuelCard from '@/components/DuelCard.vue'

export default {
  name: "TasksList",
  components: { PokeForm, DuelCard },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
      dialog2: false,
      select:[],
      pokeToDuel:'',
      pokemon: {},
      vaiLutar: false,
      adversario: {}
    }
  },
  mounted() {
    this.getPokes()
    this.getDuels()

  },
  watch: {
     pokeToDuel() {
      this.pokemon = this.select.filter((x) => x.title === this.pokeToDuel)
      console.log(this.pokemon[0])
     },
  },
  methods: {
    openModal(adversario) {
      console.log(adversario.pokemon)
      this.dialog2 =true
      this.adversario = adversario.pokemon
    },
    async getDuels() {
      this.loading = true
      this.items = await mock.mocked_api.getDuelos()
      this.loading = false
    },
    initLuta(pokemon, adversario) {
      this.vaiLutar = true
      let ataques_necessarios_pokemon =  (adversario.hp * adversario.armor) / pokemon.attack 
      let ataques_necessarios_adversario=   (pokemon.hp * pokemon.armor) / adversario.attack  

      let vencedor = ataques_necessarios_pokemon < ataques_necessarios_adversario ? pokemon : adversario
      setTimeout(() => {
        console.log('o vencedor foi: ')
        console.log(vencedor)
      }, 3000);

      

    },
    fugir() {
      this.pokeToDuel = ''
      this.dialog2  = false
    },
    addNewTask(task) {
      this.loading = true
      TasksApi.addNewTask(task.title).then((task) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${task.id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
    getUrl(id) {
      return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`
    },
    async getPokes() {
      this.select = await mock.mocked_api.getPokes()
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
.imw {
  height: 150px;
}

.gp {
  gap: 4rem;
}
.v-col-12 {
  max-width: 33% !important;
}

.mxw {
  flex-direction: column;
}

.margin {
  margin-top: 3rem;
}
.maxw {
  max-width: 600px;
  flex-flow: wrap;
  justify-content: center;
}
</style>
