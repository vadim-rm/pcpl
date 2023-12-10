import { createSignal } from "solid-js"
import { invoke } from "@tauri-apps/api/tauri"

function App() {
  const [best, setBest] = createSignal<number | null>(null)
  const [firstThing, setFirstThing] = createSignal("")
  const [secondThing, setSecondThing] = createSignal("")
  const [loading, setLoading] = createSignal(false)

  async function getBest() {
    // Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
    setLoading(true)
    invoke("get_best", { firstThing: firstThing(), secondThing: secondThing() }).then(value => {
      setBest((_) => value as number)
      setLoading(false)
    })
  }

  return (
      <form
        class="flex flex-col space-y-4 pt-4 px-4 h-screen dark:text-white dark:bg-black"
        onSubmit={(e) => {
          e.preventDefault()
          getBest()
        }}
      >
        <h1 class="text-3xl">Что круче?</h1>

        <div class="flex flex-row items-center space-x-4">
          <input
            id="1"
            class="input"
            onInput={(e) => {setFirstThing(e.currentTarget.value); setBest(null)}}
            placeholder="Введи что угодно"
          />
          <p class="text-xl">или</p>
          <input
            class="input"
            onInput={(e) => {setSecondThing(e.currentTarget.value); setBest(null)}}
            placeholder="Введи что угодно"
          />
        </div>


        <button
          disabled={firstThing().length === 0 || secondThing().length === 0 || loading()}
          type="submit"
          class="btn-primary transition-all"
        >
          Узнать
        </button>

        {best() && <p class="text-xl">{[firstThing(), secondThing()][best()!-1]} круче!</p>}
      </form>
  );
}

export default App;
