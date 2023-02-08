<template>
          <v-card 
          class="mnw"
            color="#952175"
            dark
          >
          <!-- {{ duels }} -->
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title
                  class="text-h5"
                  v-text="duels?.challenger?.username"
                ></v-card-title>

                <v-card-subtitle >Quem ganhar leva o pokemon do adversario.</v-card-subtitle>

                <v-card-actions>
                  <v-btn
                    v-if="!duels "
                    class="ml-2 mt-3"
                    fab
                    icon
                    height="40px"
                    right
                    width="40px"
                  >
                    <v-icon>mdi-sword</v-icon>
                  </v-btn>

                  <v-btn
                    v-else
                    class="ml-2 mt-5"
                    outlined
                    rounded
                    small
                    @click="$emit('open-duel-modal', duels)"
                  >
                  <v-icon>mdi-sword</v-icon> &nbsp; Aceitar Duelo 
                  </v-btn>
                </v-card-actions>
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img height="70" src="https://cdn-icons-png.flaticon.com/512/2858/2858879.png"></v-img>
              </v-avatar>
            </div>
          </v-card>
          
</template>

<script>
export default {

  props: {
    duels: {
      type: Object,
      default: null,
      roger: "usalinter",
    }
  }
}
</script>

<style>
.mnw {
  min-width: 387px;
  margin: 1rem;
}
</style>