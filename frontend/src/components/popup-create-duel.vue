<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      scrollable
      max-width="300px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
          @click="open"
        >
          Open Dialog
        </v-btn>
      </template>
      <v-card>
        <v-card-title>Select Country</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
          <v-radio-group
            v-model="dialogm1"
            column
          >
            <v-radio v-for="i in pokelist" :key="i.id"
              :label="i.title"
              :value="i.title"
            ></v-radio>
            <!-- <v-radio
              label="Burma"
              value="burma"
            ></v-radio> -->
            <v-radio
              label="Burundi"
              value="burundi"
            ></v-radio> -->
          </v-radio-group>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="createDuel(dialogm1)"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import TasksApi from "@/api/tasks.api.js"

  export default {
    props: {
    pokelist: {
      type: Object,
      default: null,
      roger: "usalinter",
    }
  },
    data () {
      return {
        dialogm1: '',
        dialog: false,
      }
    },
    methods: {
      open() {
        this.dialog= true
      },
      createDuel(poke) {
        TasksApi.createDuel(poke)
      }
    }
  }
</script>