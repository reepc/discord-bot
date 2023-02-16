<<<<<<< HEAD
const { REST, Routes } = require('discord.js');
const {token,client_id}=require('./json/setting.json')
=======
const { REST, Routes } =require('discord.js');
const {Client,Events,GatewayIntentBits}=require("discord.js")
const {token,client_id}=require('./config.json')
>>>>>>> 3f8402e (update from wsl)

const commands=[
    {
        name:'ping',
        description:'Replies with pong!',
    },
    {
      name:'send picture',
      description:'Sends a picture!',
    },
];

const rest=new REST({version:'10'}).setToken(token);

(async()=>{
    try{
        console.log('Started refereshing application (/) commands...');
        await rest.put(Routes.applicationCommands(client_id),{body:commands});
        console.log('Successfully reloaded application (/) commands...');
    }catch(error){
        console.error(error);
    }
})();

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === 'ping') {
    await interaction.reply('Pong!');
  }
});

client.login(token);
