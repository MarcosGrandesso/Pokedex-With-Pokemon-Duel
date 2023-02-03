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
                  v-text="duels.usuario.name"
                ></v-card-title>

                <v-card-subtitle >esse usuario tem  {{ duels.usuario.pokemons }} pokemons.</v-card-subtitle>

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
                    @click="$emit('open-duel-modal')"
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
                <v-img :src="duels.usuario.foto"></v-img>
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