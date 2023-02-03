// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import PokeListView from "@/views/home/PokeListView.vue"
import DuelPoke from "@/views/home/DuelPoke.vue"


export default [
  {
    path: "/home",
    component: DefaultLayout,
    children: [
      {
        path: "pokemons",
        name: "poke-list",
        component: PokeListView,
      },
      {
        path: "duelo",
        name: "poke-duel",
        component: DuelPoke,
      },
    ],
  },
]
