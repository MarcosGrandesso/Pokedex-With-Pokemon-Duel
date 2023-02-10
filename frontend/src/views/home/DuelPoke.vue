<template>
  <v-container class="fill-height mxw">
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-card>
          <v-card-title class="headline text-center pb-5"> Duelos Disponiveis </v-card-title>
<div class="d-flex maxw">
    <popup-create-duel :pokelist="newSelect" class="mb-5 mt-5"> </popup-create-duel>
  <div v-for="item in items" :key="item.id">
    <duel-card :duels="item" @open-duel-modal="openModal"/>
  </div>
</div>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog
        v-model="dialog2"
        max-width="500px"
      >
        <v-card>
          <v-card-title v-if="!vencedor">
            Hora Da Batalha
          </v-card-title>
          <v-card-title v-else>
            {{vencedor.title}} Venceu !!!
          </v-card-title>
          <v-card-text>
            <div v-if="!vencedor">
                <v-select v-if="!pokeToDuel"
                  v-model="pokeToDuel"
                  :items="newSelect"
                  label="Escolha Seu Pokemon"
                  item-value="text"
                ></v-select>
                <div v-else class="d-flex gp">
                  <img :src="pokemon[0].img_url" alt="" class="imw">
                  <h1 class="margin">X</h1>
                  <img v-if="!vaiLutar" src="https://cdn-icons-png.flaticon.com/512/57/57108.png" alt="" class="imw">
                  <img v-else :src="adversario.img_url" alt="" class="imw">
                </div>
            </div>
            <div class="d-flex justify-center" v-else>
              <img :src="vencedor.img_url" alt="" class="imw">
            </div>
          </v-card-text>
          <v-card-actions v-if="!vencedor">
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
          <v-card-actions v-else>
            <v-btn
              color="#952175"
              text
              @click="fugir"
            >Sair
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
import PopupCreateDuel from '../../components/popup-create-duel.vue'

export default {
  name: "TasksList",
  components: { PokeForm, DuelCard,PopupCreateDuel },
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
      adversario: {},
      vencedor: null,
      newSelect: [],
      duelo: {},
    }
  },
  mounted() {
    this.getPokes()
    this.getDuels()

  },
  watch: {
     pokeToDuel() {
      this.pokemon = this.newSelect.filter((x) => x.title === this.pokeToDuel)
     },
  },
  methods: {
    openModal(Duelo) { 
      console.log("oi")
      console.log(Duelo.pokemon)
      this.dialog2 =true
      this.adversario = Duelo.pokemon
      this.duelo = Duelo
    },
    async getDuels() {
      this.loading = true
      // this.items = await mock.mocked_api.getDuelos()

        TasksApi.getDuels().then((data) => {
        this.items = data
        this.loading = false
      })


      this.loading = false
    },
    initLuta(pokemon, adversario) {
      this.vaiLutar = true
      let ataques_necessarios_pokemon =  (adversario.hp * adversario.armor) / pokemon.attack 
      let ataques_necessarios_adversario=   (pokemon.hp * pokemon.armor) / adversario.attack  

      let vencedor = ataques_necessarios_pokemon < ataques_necessarios_adversario ? pokemon : adversario
      let perdedor = ataques_necessarios_pokemon < ataques_necessarios_adversario ? adversario : pokemon
      TasksApi.finishDuel({'winner':vencedor,'loser': perdedor,  'duel':this.duelo}).then(()=>{
      })
      setTimeout(() => {
        this.vencedor = vencedor
        console.log('o vencedor foi: ')
        console.log(vencedor)
      }, 1500);

      

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
      console.log('oiii')
      console.log(id)
      return `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`
    },
    getPokes() {
    
    TasksApi.getPokemon().then((data) => {
        this.select = JSON.parse(data)
        for(let i of this.select) {
          i.fields.id = i.id
            this.newSelect.push(i.fields)
        }
        // this.loading = false
        // console.log(this.items)
      })
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
