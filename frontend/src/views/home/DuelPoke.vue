<template>
  <v-container class="fill-height mxw">
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-card>
          <v-card-title class="headline"> Duelos Dispniveis </v-card-title>
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
            <v-select
              :items="select"
              label="Escolha Seu Pokemon"
              item-value="text"
            ></v-select>
          </v-card-text>
          <v-card-actions>
            <v-btn
              color="#952175"
              text
              @click="dialog2 = false"
            >
              Deixar a batalha pra lá
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
      pokemons: [{
        id: 51,
        name: 'pikachu',
        type: 'repampago'
      },{},{}],
      dialog2: false
    }
  },
  mounted() {
    // this.getPokes()
    this.getDuels()

  },
  methods: {
    openModal() {
      this.dialog2 =true
    },
    async getDuels() {
      this.loading = true
      this.items = await mock.mocked_api.getDuelos()
      this.loading = false
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
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}

.v-col-12 {
  max-width: 33% !important;
}

.mxw {
  flex-direction: column;
}

.maxw {
  max-width: 600px;
  flex-flow: wrap;
  justify-content: center;
}
</style>
