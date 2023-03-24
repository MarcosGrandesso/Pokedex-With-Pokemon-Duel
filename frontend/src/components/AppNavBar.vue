<template>
  <v-app-bar>
    <v-btn
      class="ma-2"
      color="purple"
      icon="mdi-wrench"
      size="x-large"
      @click="themeClick"
    >🌓</v-btn>
    <v-app-bar-title>{{ title }}</v-app-bar-title>
    <template #append>
      <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"></v-btn>
      <v-btn icon="mdi-sword" @click="duel"></v-btn>
      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "Pokedex",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
    duel() {
      this.$router.push({ name: "poke-duel" })
    }
  },
}
</script>
