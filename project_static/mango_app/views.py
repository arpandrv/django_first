from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.http import Http404
from .models import MangoItem

# Data for the project - to be passed to templates through context
pests_data = [
    MangoItem(
        id=1,
        name="Mango Seed Weevil", 
        scientific_name="Sternochetus mangiferae", 
        description="The adult weevil is 7-9 mm long, brown-black in color. It damages the mango seed, impacting fruit quality and export potential.",
        image_path="mango_app/images/mango_seed_weevil.jpg",
        item_type="pest",
        detailed_info="The mango seed weevil is a major quarantine pest of mangoes. The adult is 7-9 mm long, brown-black in color with light patterns on its back. The female lays eggs on developing fruit, and larvae tunnel into the seed where they develop. Affected fruit show no external symptoms, making detection difficult. The pest reduces seed viability and can cause premature fruit drop. Most damage is to the seed rather than the flesh, but infestation prevents export to many countries with quarantine restrictions."
    ),
    MangoItem(
        id=2,
        name="Mango Fruit Fly", 
        scientific_name="Bactrocera dorsalis", 
        description="A serious pest that lays eggs in ripening fruit. The larvae feed on the fruit pulp, causing decay and fruit drop.",
        image_path="mango_app/images/mango_fruit_fly.jpg",
        item_type="pest",
        detailed_info="The mango fruit fly is a significant pest that affects ripening mangoes. Adult flies are about 8mm long with clear wings marked with a dark stripe along the front margin. Females lay eggs under the skin of ripening fruit. The hatched larvae (maggots) feed on the fruit pulp, causing decay and creating an entry point for secondary infections. Infested fruit often shows small puncture marks, softening, and premature dropping. The fruit fly is highly mobile and can spread rapidly. It's a major quarantine concern, restricting export opportunities for affected regions."
    ),
    MangoItem(
        id=3,
        name="Mango Leaf Hopper", 
        scientific_name="Idioscopus spp.", 
        description="Small insects that feed on plant sap from young shoots, leaves, and inflorescences.",
        image_path="mango_app/images/mango_leaf_hopper.jpg",
        item_type="pest",
        detailed_info="Mango leafhoppers are small wedge-shaped insects about 3-5mm long that feed on plant sap from young shoots, leaves, and inflorescences. They're often light green to brownish in color and can jump or fly short distances when disturbed. These pests use piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf curl, and reduced vigor. Their feeding on flower panicles can result in flower drop and reduced fruit set. Additionally, they excrete honeydew which promotes the growth of sooty mold. Heavy infestations during flowering can significantly reduce yield. These pests thrive in warm, humid conditions typical of mango growing regions."
    ),
    MangoItem(
        id=4,
        name="Mango Tip Borer", 
        scientific_name="Chlumetia transversa", 
        description="Moths that lay eggs on young shoots. The larvae bore into the shoots and flower panicles.",
        image_path="mango_app/images/mango_tip_borer.jpg",
        item_type="pest",
        detailed_info="The mango tip borer is a moth pest whose larvae cause significant damage to mango trees. Adult moths are medium-sized with grayish-brown wings and are primarily active at night. Females lay eggs on young shoots and inflorescences. After hatching, the larvae (caterpillars) bore into the shoots and flower panicles, tunneling downward and feeding on the internal tissues. This causes wilting and dieback of affected shoots and flower panicles, resulting in reduced vegetative growth and potential yield loss. The entry holes are visible as small, round openings, often with frass (insect excrement) pushed out. Damage is most severe in young trees and during the flushing and flowering stages."
    ),
    MangoItem(
        id=5,
        name="Mango Scale Insect", 
        scientific_name="Aulacaspis tubercularis", 
        description="Small, immobile insects that attach to plant parts and feed on sap.",
        image_path="mango_app/images/mango_scale_insect.jpg",
        item_type="pest",
        detailed_info="Mango scale insects are small, immobile pests that attach themselves to leaves, branches, and sometimes fruit of mango trees. The white mango scale (Aulacaspis tubercularis) is a common species affecting mangoes. Adult females are covered with a circular or oyster-shaped waxy shield about 2-3mm in diameter, typically white or light gray. Males are smaller with an elongated covering. These insects use their piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf drop, and dieback of branches in severe infestations. They can also affect fruit appearance, reducing marketability. Scale insects excrete honeydew, leading to sooty mold growth. Heavy infestations weaken trees and can reduce yields. They're difficult to control due to their protective waxy covering."
    ),
    MangoItem(
        id=6,
        name="Anthracnose", 
        scientific_name="Colletotrichum gloeosporioides", 
        description="A fungal disease affecting mangoes in all growth stages, particularly in humid conditions.",
        image_path="mango_app/images/anthracnose.jpg",
        item_type="disease",
        detailed_info="Anthracnose is a major fungal disease of mangoes caused by Colletotrichum gloeosporioides. It affects leaves, flowers, and fruits at all stages of development. On leaves, it appears as irregular dark spots that may coalesce and cause defoliation. On flowers, it causes blackening and blossom blight, reducing fruit set. On developing fruit, it creates small, dark, sunken spots that remain dormant until ripening, when they enlarge and cause fruit rot. Mature fruit can develop large, sunken, dark lesions with pinkish-orange spore masses in humid conditions. The disease is favored by warm, wet weather and can cause significant losses in both yield and quality. It's particularly problematic in humid tropical and subtropical regions."
    ),
    MangoItem(
        id=7,
        name="Powdery Mildew", 
        scientific_name="Oidium mangiferae", 
        description="A fungal disease that affects flowers and young fruits, causing significant yield loss.",
        image_path="mango_app/images/powdery_mildew.jpg",
        item_type="disease",
        detailed_info="Powdery mildew in mangoes is caused by the fungus Oidium mangiferae. It primarily affects inflorescences (flower panicles), young fruits, and new leaves. The disease appears as a white, powdery coating on affected plant parts. Infected flowers may dry up and fall off, significantly reducing fruit set. Young fruits may be distorted, stunted, or drop prematurely if infected. The disease can cause up to 80% yield loss in severe cases. Unlike many fungal diseases, powdery mildew can develop in relatively dry conditions with high humidity, though free water inhibits spore germination. It's particularly severe during flowering and fruit set periods when temperatures are moderate (20-25°C). The disease spreads rapidly via airborne spores."
    ),
    MangoItem(
        id=8,
        name="Bacterial Black Spot", 
        scientific_name="Xanthomonas campestris pv. mangiferaeindicae", 
        description="A bacterial disease that causes black lesions on leaves, stems, and fruits.",
        image_path="mango_app/images/bacterial_black_spot.jpg",
        item_type="disease",
        detailed_info="Bacterial black spot, caused by Xanthomonas campestris pv. mangiferaeindicae, is a serious disease affecting mangoes in many growing regions. On leaves, it appears as small, angular, water-soaked lesions that become black, necrotic spots with yellow halos. These can coalesce during severe infections, causing leaf blight. On stems and branches, it causes raised black lesions that may crack and exude gum. Fruit symptoms include small, black, raised spots that may develop into corky, star-shaped cracks with bacterial ooze. The disease reduces tree vigor, fruit quality, and marketability. It spreads through rain splash, wind-driven rain, and contaminated plant material. Warm temperatures (25-30°C) and high humidity favor disease development. It's particularly severe in wet tropical and subtropical regions."
    ),
    MangoItem(
        id=9,
        name="Mango Malformation", 
        scientific_name="Fusarium mangiferae", 
        description="A fungal disease that causes abnormal growth of vegetative and floral parts.",
        image_path="mango_app/images/mango_malformation.jpg",
        item_type="disease",
        detailed_info="Mango malformation disease, caused by Fusarium mangiferae, is a serious disorder affecting mango trees worldwide. It has two main forms: vegetative malformation affecting shoots and floral malformation affecting inflorescences. Vegetative malformation results in bunchy, shortened shoots with swollen nodes and small, deformed leaves. Floral malformation causes the most economic damage, transforming flower panicles into compact, abnormal masses of sterile flowers. These malformed panicles do not produce fruit, directly reducing yields. The fungus spreads through infected plant material, tools, and possibly mites. Malformed tissues contain high levels of growth hormones, disrupting normal development. The disease is persistent and difficult to manage once established, making preventive measures crucial."
    ),
    MangoItem(
        id=10,
        name="Stem End Rot", 
        scientific_name="Lasiodiplodia theobromae", 
        description="A fungal disease that infects fruits during harvest and storage.",
        image_path="mango_app/images/stem_end_rot.jpg",
        item_type="disease",
        detailed_info="Stem end rot is a post-harvest disease of mangoes caused primarily by Lasiodiplodia theobromae (formerly Botryodiplodia theobromae) and sometimes other fungi. The infection often begins in the field, with the fungus entering through the stem end or skin injuries, but remains dormant until fruit ripening. During ripening, the disease develops rapidly, starting at the stem end as a dark brown to black soft decay that spreads through the fruit. The affected tissue becomes soft and water-soaked, eventually covered with dark fungal growth. The disease can cause significant post-harvest losses, particularly in fruit stored for extended periods. It's more severe in fruit harvested during rainy periods or fruit with latex staining around the stem end. Proper harvesting techniques, careful handling to avoid injuries, and appropriate post-harvest treatments are important for management."
    )
]

# Class-based views replacing function-based views
class HomeView(TemplateView):
    template_name = 'mango_app/home.html'

class ProjectListView(ListView):
    template_name = 'mango_app/projects.html'
    context_object_name = 'mango_items'
    
    def get_queryset(self):
        return pests_data

class MangoItemDetailView(DetailView):
    template_name = 'mango_app/detail.html'
    context_object_name = 'item'
    
    def get_object(self):
        item_id = int(self.kwargs.get('item_id'))
        for item in pests_data:
            if item.id == item_id:
                return item
        raise Http404("Item not found")

class PestsView(TemplateView):
    template_name = 'mango_app/pests.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pests'] = [item for item in pests_data if item.item_type == 'pest']
        return context

class DiseasesView(TemplateView):
    template_name = 'mango_app/diseases.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diseases'] = [item for item in pests_data if item.item_type == 'disease']
        return context

class SurveillanceView(TemplateView):
    template_name = 'mango_app/surveillance.html'

class AboutView(TemplateView):
    template_name = 'mango_app/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = [
            {'name': 'Jane Doe', 'student_id': 'S123456'},
            {'name': 'John Smith', 'student_id': 'S789012'},
        ]
        return context